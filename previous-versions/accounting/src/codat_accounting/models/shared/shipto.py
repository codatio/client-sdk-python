"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .items import Items, ItemsTypedDict
from codat_accounting.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class ShipToContactTypedDict(TypedDict):
    r"""Details of the named contact at the delivery address."""

    email: NotRequired[Nullable[str]]
    r"""Email address of the contact at the delivery address."""
    name: NotRequired[Nullable[str]]
    r"""Name of the contact at the delivery address."""
    phone: NotRequired[Nullable[str]]
    r"""Phone number of the contact at the delivery address."""


class ShipToContact(BaseModel):
    r"""Details of the named contact at the delivery address."""

    email: OptionalNullable[str] = UNSET
    r"""Email address of the contact at the delivery address."""

    name: OptionalNullable[str] = UNSET
    r"""Name of the contact at the delivery address."""

    phone: OptionalNullable[str] = UNSET
    r"""Phone number of the contact at the delivery address."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["email", "name", "phone"]
        nullable_fields = ["email", "name", "phone"]
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


class ShipToTypedDict(TypedDict):
    r"""Delivery details for any goods that have been ordered."""

    address: NotRequired[ItemsTypedDict]
    contact: NotRequired[ShipToContactTypedDict]
    r"""Details of the named contact at the delivery address."""


class ShipTo(BaseModel):
    r"""Delivery details for any goods that have been ordered."""

    address: Optional[Items] = None

    contact: Optional[ShipToContact] = None
    r"""Details of the named contact at the delivery address."""
