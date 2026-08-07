"""Freeform content object. Synthesized to match Speakeasy's shared surface."""
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing_extensions import NotRequired, TypedDict


class ContentTypedDict(TypedDict):
    pass


class Content(BaseModel):
    @model_serializer(mode="wrap")
    def _serialize_drop_none(self, handler):
        serialized = handler(self)
        return {k: v for k, v in serialized.items() if v is not None}

    def to_dict(self):
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj):
        return cls.model_validate(obj) if obj is not None else None

    pass

    model_config = ConfigDict(populate_by_name=True, extra="allow", protected_namespaces=())
