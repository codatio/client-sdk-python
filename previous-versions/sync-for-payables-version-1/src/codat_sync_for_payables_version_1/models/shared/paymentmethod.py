"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .metadata import Metadata, MetadataTypedDict
from .paymentmethodtype import PaymentMethodType
from codat_sync_for_payables_version_1.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PaymentMethodStatus(str, Enum):
    r"""Status of the Payment Method."""

    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"


class PaymentMethodTypedDict(TypedDict):
    r"""> View the coverage for payment methods in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=paymentMethods\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    A Payment Method represents the payment method(s) used to pay a Bill. Payment Methods are referenced on [Bill Payments](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) and [Payments](https://docs.codat.io/sync-for-payables-api#/schemas/Payment).
    """

    id: NotRequired[str]
    r"""Unique identifier for the payment method."""
    metadata: NotRequired[MetadataTypedDict]
    modified_date: NotRequired[str]
    name: NotRequired[Nullable[str]]
    r"""Name of the payment method."""
    source_modified_date: NotRequired[str]
    status: NotRequired[PaymentMethodStatus]
    r"""Status of the Payment Method."""
    type: NotRequired[PaymentMethodType]
    r"""Method of payment."""


class PaymentMethod(BaseModel):
    r"""> View the coverage for payment methods in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=paymentMethods\" target=\"_blank\">Data coverage explorer</a>.

    ## Overview

    A Payment Method represents the payment method(s) used to pay a Bill. Payment Methods are referenced on [Bill Payments](https://docs.codat.io/sync-for-payables-api#/schemas/BillPayment) and [Payments](https://docs.codat.io/sync-for-payables-api#/schemas/Payment).
    """

    id: Optional[str] = None
    r"""Unique identifier for the payment method."""

    metadata: Optional[Metadata] = None

    modified_date: Annotated[Optional[str], pydantic.Field(alias="modifiedDate")] = None

    name: OptionalNullable[str] = UNSET
    r"""Name of the payment method."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    status: Optional[PaymentMethodStatus] = None
    r"""Status of the Payment Method."""

    type: Optional[PaymentMethodType] = None
    r"""Method of payment."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "metadata",
            "modifiedDate",
            "name",
            "sourceModifiedDate",
            "status",
            "type",
        ]
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
