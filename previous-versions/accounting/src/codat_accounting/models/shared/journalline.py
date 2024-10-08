"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountref import AccountRef, AccountRefTypedDict
from .propertie_tracking2 import PropertieTracking2, PropertieTracking2TypedDict
from codat_accounting.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_accounting.utils import serialize_decimal, validate_decimal
from decimal import Decimal
from enum import Enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class JournalLineDataType(str, Enum):
    r"""Allowed name of the 'dataType'."""

    CUSTOMERS = "customers"
    SUPPLIERS = "suppliers"


class ContactReferenceTypedDict(TypedDict):
    id: str
    r"""Unique identifier for a customer or supplier."""
    data_type: NotRequired[Nullable[JournalLineDataType]]
    r"""Allowed name of the 'dataType'."""


class ContactReference(BaseModel):
    id: str
    r"""Unique identifier for a customer or supplier."""

    data_type: Annotated[
        OptionalNullable[JournalLineDataType], pydantic.Field(alias="dataType")
    ] = UNSET
    r"""Allowed name of the 'dataType'."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["dataType"]
        nullable_fields = ["dataType"]
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


class JournalLineTypedDict(TypedDict):
    net_amount: Decimal
    r"""Amount for the journal line. Debit entries are considered positive, and credit entries are considered negative."""
    account_ref: NotRequired[AccountRefTypedDict]
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    contact_ref: NotRequired[ContactReferenceTypedDict]
    currency: NotRequired[Nullable[str]]
    r"""Currency for the journal line item."""
    description: NotRequired[Nullable[str]]
    r"""Description of the journal line item."""
    tracking: NotRequired[PropertieTracking2TypedDict]


class JournalLine(BaseModel):
    net_amount: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="netAmount"),
    ]
    r"""Amount for the journal line. Debit entries are considered positive, and credit entries are considered negative."""

    account_ref: Annotated[Optional[AccountRef], pydantic.Field(alias="accountRef")] = (
        None
    )
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""

    contact_ref: Annotated[
        Optional[ContactReference], pydantic.Field(alias="contactRef")
    ] = None

    currency: OptionalNullable[str] = UNSET
    r"""Currency for the journal line item."""

    description: OptionalNullable[str] = UNSET
    r"""Description of the journal line item."""

    tracking: Optional[PropertieTracking2] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "accountRef",
            "contactRef",
            "currency",
            "description",
            "tracking",
        ]
        nullable_fields = ["currency", "description"]
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
