"""Report generation webhook. Synthesized to match Speakeasy's shared surface."""
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing_extensions import NotRequired, TypedDict
from codat_lending.models.shared.reportgenerationpayload import ReportGenerationPayload, ReportGenerationPayloadTypedDict


class SchemaTypedDict(TypedDict):
    id: NotRequired[Optional[str]]
    event_type: NotRequired[Optional[str]]
    generated_date: NotRequired[Optional[str]]
    payload: NotRequired[Optional[ReportGenerationPayloadTypedDict]]


class Schema(BaseModel):
    @model_serializer(mode="wrap")
    def _serialize_drop_none(self, handler):
        serialized = handler(self)
        return {k: v for k, v in serialized.items() if v is not None}

    def to_dict(self):
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj):
        return cls.model_validate(obj) if obj is not None else None

    id: Optional[str] = None
    event_type: Optional[str] = Field(default=None, alias="eventType")
    generated_date: Optional[str] = Field(default=None, alias="generatedDate")
    payload: Optional[ReportGenerationPayload] = None

    model_config = ConfigDict(populate_by_name=True, protected_namespaces=())
