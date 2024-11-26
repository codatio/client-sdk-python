"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .servicechargetype import ServiceChargeType
from .taxcomponentallocation import (
    TaxComponentAllocation,
    TaxComponentAllocationTypedDict,
)
from codat_lending.types import BaseModel
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ServiceChargeTypedDict(TypedDict):
    description: NotRequired[str]
    r"""Service charges for this order."""
    quantity: NotRequired[int]
    r"""The number of times the charge is charged."""
    tax_amount: NotRequired[Decimal]
    r"""Amount of the service charge that is tax."""
    tax_percentage: NotRequired[Decimal]
    r"""Percentage rate (from 0 to 100) of any tax applied to the service charge."""
    taxes: NotRequired[List[TaxComponentAllocationTypedDict]]
    r"""Taxes breakdown as applied to service charges."""
    total_amount: NotRequired[Decimal]
    r"""Total amount of the service charge, including tax."""
    type: NotRequired[ServiceChargeType]
    r"""The type of the service charge."""


class ServiceCharge(BaseModel):
    description: Optional[str] = None
    r"""Service charges for this order."""

    quantity: Optional[int] = None
    r"""The number of times the charge is charged."""

    tax_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="taxAmount"),
    ] = None
    r"""Amount of the service charge that is tax."""

    tax_percentage: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="taxPercentage"),
    ] = None
    r"""Percentage rate (from 0 to 100) of any tax applied to the service charge."""

    taxes: Optional[List[TaxComponentAllocation]] = None
    r"""Taxes breakdown as applied to service charges."""

    total_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalAmount"),
    ] = None
    r"""Total amount of the service charge, including tax."""

    type: Optional[ServiceChargeType] = None
    r"""The type of the service charge."""