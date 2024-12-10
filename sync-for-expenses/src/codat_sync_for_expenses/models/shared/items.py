"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountingaddresstype import AccountingAddressType
from codat_sync_for_expenses.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class ItemsTypedDict(TypedDict):
    type: AccountingAddressType
    r"""The type of the address"""
    city: NotRequired[Nullable[str]]
    r"""City of the customer address."""
    country: NotRequired[Nullable[str]]
    r"""Country of the customer address."""
    line1: NotRequired[Nullable[str]]
    r"""Line 1 of the customer address."""
    line2: NotRequired[Nullable[str]]
    r"""Line 2 of the customer address."""
    postal_code: NotRequired[Nullable[str]]
    r"""Postal code or zip code."""
    region: NotRequired[Nullable[str]]
    r"""Region of the customer address."""


class Items(BaseModel):
    type: AccountingAddressType
    r"""The type of the address"""

    city: OptionalNullable[str] = UNSET
    r"""City of the customer address."""

    country: OptionalNullable[str] = UNSET
    r"""Country of the customer address."""

    line1: OptionalNullable[str] = UNSET
    r"""Line 1 of the customer address."""

    line2: OptionalNullable[str] = UNSET
    r"""Line 2 of the customer address."""

    postal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="postalCode")
    ] = UNSET
    r"""Postal code or zip code."""

    region: OptionalNullable[str] = UNSET
    r"""Region of the customer address."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["city", "country", "line1", "line2", "postalCode", "region"]
        nullable_fields = ["city", "country", "line1", "line2", "postalCode", "region"]
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