"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class ValidationItemTypedDict(TypedDict):
    item_id: NotRequired[Nullable[str]]
    r"""Unique identifier for a validation item."""
    message: NotRequired[Nullable[str]]
    r"""A message outlining validation item's issue."""
    validator_name: NotRequired[Nullable[str]]
    r"""Name of validator."""


class ValidationItem(BaseModel):
    item_id: Annotated[OptionalNullable[str], pydantic.Field(alias="itemId")] = UNSET
    r"""Unique identifier for a validation item."""

    message: OptionalNullable[str] = UNSET
    r"""A message outlining validation item's issue."""

    validator_name: Annotated[
        OptionalNullable[str], pydantic.Field(alias="validatorName")
    ] = UNSET
    r"""Name of validator."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["itemId", "message", "validatorName"]
        nullable_fields = ["itemId", "message", "validatorName"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
