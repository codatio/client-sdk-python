"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class TransactionCategoryRefTypedDict(TypedDict):
    r"""An object of bank transaction category reference data."""

    id: str
    r"""The unique category reference id for the bank transaction."""
    name: NotRequired[Nullable[str]]
    r"""The category name reference for the bank transaction."""


class TransactionCategoryRef(BaseModel):
    r"""An object of bank transaction category reference data."""

    id: str
    r"""The unique category reference id for the bank transaction."""

    name: OptionalNullable[str] = UNSET
    r"""The category name reference for the bank transaction."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name"]
        nullable_fields = ["name"]
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
