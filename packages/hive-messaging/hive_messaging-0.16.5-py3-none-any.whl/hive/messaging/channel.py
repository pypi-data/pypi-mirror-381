from __future__ import annotations

import json
import logging

from datetime import datetime, timedelta, timezone
from dataclasses import KW_ONLY, dataclass
from functools import cache, cached_property
from typing import Any, Literal, Optional, TYPE_CHECKING

from cloudevents.pydantic import CloudEvent
from cloudevents.conversion import to_json

from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel as _PikaChannel
from pika.delivery_mode import DeliveryMode  # type: ignore

from pydantic import BaseModel

from hive.common import SERVICE_NAME, utc_now

from .message import Message
from .semantics import Semantics

if TYPE_CHECKING:
    from .typing import ConsumerTag, OnMessageCallback

logger = logging.getLogger(__name__)


@dataclass
class Channel:
    """The primary entry point for interacting with Hive's message bus.
    """
    _pika: _PikaChannel
    _: KW_ONLY
    name: str = ""

    def __hash__(self) -> int:
        return id(self)

    # Messages are:
    #  - PUBLISHED to EXCHANGES
    #  - CONSUMED from QUEUES
    #
    # QUEUES are declared (created) by their consuming service;
    # EXCHANGES are declared by both consumers and publishers.
    #
    # REQUESTS are things we're asking to be done.  They have competing-
    # consumers semantics:
    #  - Multiple services may consume one requests queue
    #  - Each message should be consumed by exactly one service
    #
    # EVENTS are things that have happened.  The have publish-subscribe
    # semantics:
    # - Each events queue *should be* consumed by exactly one
    #   consumer, but note that this isn't enforced;  hive-messaging
    #   prior to 0.10.0 used exclusive queues for these semantics,
    #   but exclusive queues can't be durable so hive-messaging now
    #   0.10.0 declares all queues as durable and tries to create
    #   exclusive queues by prefixing their names.
    # - Each message is received by each consuming service.
    #
    # CONSUME_* methods process to completion or dead-letter the message.

    def publish_request(self, **kwargs: Any) -> None:
        self._publish(mandatory=True, **kwargs)

    def publish_event(self, **kwargs: Any) -> None:
        self._publish(**kwargs)

    def maybe_publish_event(self, **kwargs: Any) -> None:
        try:
            self.publish_event(**kwargs)
        except Exception:
            logger.warning("EXCEPTION", exc_info=True)

    def consume_requests(self, **kwargs: Any) -> None:
        self._consume(Semantics.COMPETING_CONSUMERS, **kwargs)

    def consume_events(self, **kwargs: Any) -> None:
        self._consume(Semantics.PUBLISH_SUBSCRIBE, **kwargs)

    def start_consuming(self) -> None:
        self._pika.start_consuming()

    # Lower-level handlers for PUBLISH_* and CONSUME_*
    #  - Everything should go through these
    #  - XXX merge _consume into *basic_consume*?

    def _publish(
            self,
            *,
            routing_key: str,
            topic: str = "",
            correlation_id: Optional[str] = None,
            mandatory: bool = False,
            consume_by: Optional[datetime] = None,
            **kwargs: Any,
    ) -> None:
        payload, content_type = self._encapsulate(routing_key, **kwargs)

        exchange = self._exchange_for(routing_key, topic)
        routing_key = topic

        properties = {
            "content_type": content_type,
            "correlation_id": correlation_id,
            "delivery_mode": DeliveryMode.Persistent,
        }

        if consume_by:
            ttl = consume_by - datetime.now(tz=timezone.utc)
            ttl_ms = round(ttl / timedelta(milliseconds=1))
            properties["expiration"] = str(ttl_ms)

        self._pika.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=payload,
            properties=BasicProperties(**properties),
            mandatory=mandatory,
        )

    def _consume(
            self,
            semantics: Semantics,
            *,
            queue: str,
            on_message_callback: OnMessageCallback,
            exclusive: bool = False,
            topic: str = "",
    ) -> ConsumerTag:
        exchange = self._exchange_for(queue, topic)

        if semantics is Semantics.PUBLISH_SUBSCRIBE:
            if (prefix := self.consumer_name):
                queue = f"{prefix}.{queue}"

        kwargs: dict[str, Any] = {}
        if exclusive:
            kwargs["exclusive"] = True
        else:
            kwargs["durable"] = True
            kwargs["dead_letter_routing_key"] = queue

        self.queue_declare(queue, **kwargs)

        kwargs = {}
        if topic:
            kwargs["routing_key"] = topic

        self._pika.queue_bind(queue=queue, exchange=exchange, **kwargs)

        return self._basic_consume(queue, on_message_callback)

    # Queue-name disambiguation for consume_events().

    @cached_property
    def consumer_name(self) -> str:
        """Name for per-consumer fanout queues to this channel.

        May be overwritten or overridden.  You may need this to avoid
        competing consumers on fanout "queue"s, though using named
        channels to ensure unique names is preferable.
        """
        parts = list(SERVICE_NAME.split("-"))
        if (channel_name := self.name):
            parts.append(channel_name)
        return ".".join(parts)

    # Exchanges

    @cache
    def _exchange_for(self, routing_key: str, topic: str) -> str:
        return self._hive_exchange(
            exchange=routing_key,
            exchange_type="topic" if topic else "fanout",
            durable=True,
        )

    @cached_property
    def dead_letter_exchange(self) -> str:
        return self._hive_exchange(
            exchange="dead.letter",
            exchange_type="direct",
            durable=True,
        )

    def _hive_exchange(self, exchange: str, **kwargs: Any) -> str:
        name = f"hive.{exchange}"
        self._pika.exchange_declare(exchange=name, **kwargs)
        return name

    # Queues

    def queue_declare(
            self,
            queue: str,
            *,
            dead_letter_routing_key: Optional[str] = None,
            arguments: Optional[dict[str, str]] = None,
            **kwargs: Any
    ) -> None:
        if dead_letter_routing_key:
            DLX_ARG = "x-dead-letter-exchange"
            if arguments:
                if DLX_ARG in arguments:
                    raise ValueError(arguments)
                arguments = arguments.copy()
            else:
                arguments = {}

            dead_letter_queue = f"x.{dead_letter_routing_key}"
            self._pika.queue_declare(
                dead_letter_queue,
                durable=True,
            )

            dead_letter_exchange = self.dead_letter_exchange
            self._pika.queue_bind(
                queue=dead_letter_queue,
                exchange=dead_letter_exchange,
                routing_key=dead_letter_routing_key,
            )

            arguments[DLX_ARG] = dead_letter_exchange

        if arguments:
            kwargs["arguments"] = arguments
        self._pika.queue_declare(queue, **kwargs)

    @classmethod
    def _encapsulate(
            cls,
            routing_key: str,
            **kwargs: Any
    ) -> tuple[bytes, str]:
        """Prepare messages for transmission.
        """
        message = kwargs.pop("message", None)
        if message is None:
            message = cls._encapsulate_new(routing_key, **kwargs)
            kwargs = {}

        content_type = kwargs.pop("content_type", None)
        if kwargs:
            raise ValueError(kwargs)

        return cls._encapsulate_old(message, content_type)

    @staticmethod
    def _encapsulate_new(
            routing_key: str,
            *,
            source: Optional[str] = None,
            type: Optional[str] = None,
            time: Optional[datetime] = None,
            **kwargs: Any
    ) -> CloudEvent:
        """Prepare messages for transmission.
        """
        if not source:
            source = f"https://gbenson.net/hive/services/{SERVICE_NAME}"
        if not type:
            type = "net.gbenson.hive." + (
                routing_key
                .removesuffix("s")
                .removesuffix("e")
                .replace(".", "_")
            )
        if not time:
            time = utc_now()
        if isinstance((data := kwargs.get("data")), BaseModel):
            kwargs["data"] = json.loads(data.model_dump_json())
        return CloudEvent(source=source, type=type, time=time, **kwargs)

    @staticmethod
    def _encapsulate_old(
            msg: bytes | dict[str, Any] | CloudEvent,
            content_type: Optional[str],
    ) -> tuple[bytes, str]:
        """Prepare messages for transmission.
        """
        if isinstance(msg, CloudEvent):
            return to_json(msg), "application/cloudevents+json"
        if not isinstance(msg, bytes):
            return json.dumps(msg).encode("utf-8"), "application/json"
        if not content_type:
            raise ValueError(f"content_type={content_type}")
        return msg, content_type

    @property
    def prefetch_count(self) -> Optional[int]:
        return getattr(self, "_prefetch_count", None)

    @prefetch_count.setter
    def prefetch_count(self, value: int) -> None:
        if self.prefetch_count == value:
            return
        if self.prefetch_count is not None:
            raise ValueError(value)
        self._pika.basic_qos(prefetch_count=value)
        self._prefetch_count = value

    def _basic_consume(
            self,
            queue: str,
            on_message_callback: OnMessageCallback,
    ) -> ConsumerTag:
        self.prefetch_count = 1  # Receive one message at a time.

        def _wrapped_callback(channel: Channel, message: Message) -> None:
            delivery_tag = message.method.delivery_tag
            assert delivery_tag is not None
            try:
                on_message_callback(channel, message)
                channel._pika.basic_ack(delivery_tag=delivery_tag)

            except Exception as e:
                channel._pika.basic_reject(
                    delivery_tag=delivery_tag,
                    requeue=False,
                )
                logged = False
                try:
                    if isinstance(e, NotImplementedError) and e.args:
                        if (traceback := e.__traceback__):
                            while (next_tb := traceback.tb_next):
                                traceback = next_tb
                            code = traceback.tb_frame.f_code
                            try:
                                func = getattr(code, "co_qualname")
                            except AttributeError:
                                func = code.co_name  # Python <=3.10
                            logger.warning("%s:%s:UNHANDLED", func, e)
                            logged = True

                except Exception:
                    logger.exception("NESTED EXCEPTION")
                if not logged:
                    logger.exception("EXCEPTION")

        return self._basic_consume_raw(queue, _wrapped_callback)

    def _basic_consume_raw(
            self,
            queue: str,
            on_message_callback: OnMessageCallback,
    ) -> ConsumerTag:
        def _wrapped_callback(
                channel: _PikaChannel,
                *args: Any,
                **kwargs: Any,
        ) -> None:
            assert channel is self._pika
            on_message_callback(self, Message(*args, **kwargs))

        return self._pika.basic_consume(
            queue=queue,
            on_message_callback=_wrapped_callback,
        )

    # High-level publish_request wrappers for Matrix chat.

    def send_text(
            self,
            text: str = "",
            *,
            html: str = "",
            sender: str = "hive",
    ) -> None:
        """https://pkg.go.dev/maunium.net/go/mautrix#Client.SendText
        """
        if not text and not html:
            raise ValueError

        self.publish_matrix_event("send_text", {
            "sender": sender,
            "text": text,
            "html": html,
        })

    tell_user = send_text

    def send_reaction(
            self,
            reaction: str,
            *,
            in_reply_to: str | CloudEvent,
            sender: str = "hive",
    ) -> None:
        """https://pkg.go.dev/maunium.net/go/mautrix#Client.SendReaction
        """
        if not reaction:
            raise ValueError

        if isinstance(in_reply_to, CloudEvent):
            in_reply_to = in_reply_to.id

        if not in_reply_to:
            raise ValueError

        self.publish_matrix_event("send_reaction", {
            "event_id": in_reply_to,
            "reaction": reaction,
            "sender": sender,
        })

    def set_user_typing(
            self,
            timeout: timedelta | Literal[False],
            *,
            sender: str = "hive",
    ) -> None:
        """https://pkg.go.dev/maunium.net/go/mautrix#Client.UserTyping
        """
        nanos = round(timeout.total_seconds() * 1e9) if timeout else 0
        self.maybe_publish_matrix_event("user_typing", {
            "sender": sender,
            "timeout": nanos,
        })

    # Low(er)-level publish_request wrappers for Matrix chat.
    #
    # Event? Request?  The end goal is a published Matrix EVENT,
    # but what we publish is a Hive messaging REQUEST, to the
    # matrix-connector service.  TL;dr either name could make
    # sense here!

    def publish_matrix_event(
            self,
            event_type: str,
            event_data: dict[str, Any],
    ) -> None:
        self.publish_request(
            type=f"net.gbenson.hive.matrix_{event_type}_request",
            data={k: v for k, v in event_data.items() if v or v == 0},
            routing_key="matrix.requests",
        )

    def maybe_publish_matrix_event(self, *args: Any, **kwargs: Any) -> None:
        try:
            return self.publish_matrix_event(*args, **kwargs)
        except Exception:
            logger.warning("EXCEPTION", exc_info=True)
