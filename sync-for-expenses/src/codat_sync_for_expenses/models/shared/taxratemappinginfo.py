"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .validtransactiontypes import ValidTransactionTypes
from codat_sync_for_expenses.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_sync_for_expenses.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TaxRateMappingInfoTypedDict(TypedDict):
    code: NotRequired[Nullable[str]]
    r"""Code for the tax rate from the accounting software."""
    effective_tax_rate: NotRequired[Decimal]
    r"""Effective tax rate."""
    id: NotRequired[str]
    r"""Unique identifier of tax rate."""
    name: NotRequired[str]
    r"""Name of the tax rate in the accounting software."""
    total_tax_rate: NotRequired[Decimal]
    r"""Total (not compounded) sum of the components of a tax rate."""
    valid_transaction_types: NotRequired[List[ValidTransactionTypes]]
    r"""Supported transaction types for the account."""


class TaxRateMappingInfo(BaseModel):
    code: OptionalNullable[str] = UNSET
    r"""Code for the tax rate from the accounting software."""

    effective_tax_rate: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="effectiveTaxRate"),
    ] = None
    r"""Effective tax rate."""

    id: Optional[str] = None
    r"""Unique identifier of tax rate."""

    name: Optional[str] = None
    r"""Name of the tax rate in the accounting software."""

    total_tax_rate: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalTaxRate"),
    ] = None
    r"""Total (not compounded) sum of the components of a tax rate."""

    valid_transaction_types: Annotated[
        Optional[List[ValidTransactionTypes]],
        pydantic.Field(alias="validTransactionTypes"),
    ] = None
    r"""Supported transaction types for the account."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "code",
            "effectiveTaxRate",
            "id",
            "name",
            "totalTaxRate",
            "validTransactionTypes",
        ]
        nullable_fields = ["code"]
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