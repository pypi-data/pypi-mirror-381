import json

from dataclasses import dataclass
from typing import Any, Optional

from cloudevents.pydantic import CloudEvent
from contenttype import ContentType  # type: ignore
from pika.spec import Basic, BasicProperties


@dataclass
class Message:
    method: Basic.Deliver
    properties: BasicProperties
    body: bytes

    @property
    def correlation_id(self) -> Optional[str]:
        return self.properties.correlation_id

    @property
    def content_type(self) -> Optional[str]:
        return self.properties.content_type

    @property
    def is_json(self) -> bool:
        ct = ContentType.parse(self.content_type)
        if ct.type != "application":
            return False
        if ct.subtype == "json":
            return True
        return str(ct.suffix) == "json"

    def json(self) -> Any:
        if not self.is_json:
            raise ValueError(self.content_type)
        return json.loads(self.body)

    @property
    def is_cloudevent(self) -> bool:
        ct = ContentType.parse(self.content_type)
        return str(ct.type) == "application" \
            and str(ct.subtype) == "cloudevents"

    def event(self) -> CloudEvent:
        if not self.is_cloudevent:
            raise ValueError(self.content_type)
        if not self.is_json:
            raise NotImplementedError(self.content_type)
        return CloudEvent.model_validate_json(self.body)
