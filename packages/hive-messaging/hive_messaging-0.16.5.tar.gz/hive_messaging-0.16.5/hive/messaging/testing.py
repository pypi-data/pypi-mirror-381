from dataclasses import dataclass, field
from typing import Any, Optional, Protocol
from unittest.mock import Mock

import pytest

from cloudevents.abstract import CloudEvent

from .connection import Connection
from .message import Message
from .message_bus import MessageBus


class ConnectionFactory(Protocol):
    def __call__(self, **kwargs: Any) -> Connection: ...


@pytest.fixture
def blocking_connection() -> ConnectionFactory:
    def connect(**kwargs: Any) -> Connection:
        kwargs["connection_attempts"] = 1
        try:
            return MessageBus().blocking_connection(**kwargs)
        except KeyError:
            pytest.skip("Message bus not configured")
        except ConnectionRefusedError as e:
            pytest.skip(f"Message bus not available: {e}")
    return connect


@dataclass(frozen=True)
class ChannelCall:
    method: str
    routing_key: str
    message: Message
    event: Optional[CloudEvent]


@dataclass(frozen=True)
class LogDecoder:
    call_log: list[ChannelCall]


@dataclass(frozen=True)
class MockChannel:
    log_decoder: type[LogDecoder] = LogDecoder
    call_log: list[ChannelCall] = field(default_factory=list)

    def __getattr__(self, attr: str) -> Any:
        return MockMethod(attr, self.call_log)

    @property
    def expect(self) -> LogDecoder:
        return self.log_decoder(self.call_log)


@dataclass(frozen=True)
class MockMethod:
    name: str
    _call_log: list[ChannelCall]

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        if self.name != "basic_publish":
            return
        assert not args
        assert not kwargs.pop("routing_key")
        routing_key = kwargs.pop("exchange")
        mandatory = kwargs.pop("mandatory", False)
        name = "publish_request" if mandatory else "publish_event"
        message = Message(method=Mock(), **kwargs)
        try:
            event = message.event()
        except Exception:
            event = None
        self._call_log.append(ChannelCall(name, routing_key, message, event))
