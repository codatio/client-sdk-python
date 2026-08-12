"""A validation item. Synthesized to match Speakeasy's shared surface."""
from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing_extensions import NotRequired, TypedDict


class ValidationItem1TypedDict(TypedDict):
    item_id: NotRequired[Optional[str]]
    message: NotRequired[Optional[str]]
    rule_id: NotRequired[Optional[str]]
    validator_name: NotRequired[Optional[str]]


class ValidationItem1(BaseModel):
    @model_serializer(mode="wrap")
    def _serialize_drop_none(self, handler):
        serialized = handler(self)
        return {k: v for k, v in serialized.items() if v is not None}

    def to_dict(self):
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj):
        return cls.model_validate(obj) if obj is not None else None

    item_id: Optional[str] = Field(default=None, alias="itemId")
    message: Optional[str] = None
    rule_id: Optional[str] = Field(default=None, alias="ruleId")
    validator_name: Optional[str] = Field(default=None, alias="validatorName")

    model_config = ConfigDict(populate_by_name=True, protected_namespaces=())
