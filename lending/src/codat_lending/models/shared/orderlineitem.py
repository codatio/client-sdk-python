"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .orderdiscountallocation import (
    OrderDiscountAllocation,
    OrderDiscountAllocationTypedDict,
)
from .productref import ProductRef, ProductRefTypedDict
from .productvariantref import ProductVariantRef, ProductVariantRefTypedDict
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


class OrderLineItemTypedDict(TypedDict):
    id: str
    r"""A unique, persistent identifier for this record"""
    discount_allocations: NotRequired[List[OrderDiscountAllocationTypedDict]]
    product_ref: NotRequired[ProductRefTypedDict]
    r"""Reference that links the line item to the correct product details."""
    product_variant_ref: NotRequired[ProductVariantRefTypedDict]
    r"""Reference that links the line item to the specific version of product that has been ordered."""
    quantity: NotRequired[Decimal]
    r"""Number of units of the product sold.
    For refunds, quantity is negative.

    """
    tax_percentage: NotRequired[Decimal]
    r"""Percentage rate (from 0 to 100) of any sales tax applied to the unit price."""
    taxes: NotRequired[List[TaxComponentAllocationTypedDict]]
    r"""Taxes breakdown as applied to order lines."""
    total_amount: NotRequired[Decimal]
    r"""Total amount of the line item, including discounts and tax."""
    total_tax_amount: NotRequired[Decimal]
    r"""Total amount of tax applied to the line item, factoring in any discounts."""
    unit_price: NotRequired[Decimal]
    r"""Price per unit of goods or services, excluding discounts and tax."""


class OrderLineItem(BaseModel):
    id: str
    r"""A unique, persistent identifier for this record"""

    discount_allocations: Annotated[
        Optional[List[OrderDiscountAllocation]],
        pydantic.Field(alias="discountAllocations"),
    ] = None

    product_ref: Annotated[Optional[ProductRef], pydantic.Field(alias="productRef")] = (
        None
    )
    r"""Reference that links the line item to the correct product details."""

    product_variant_ref: Annotated[
        Optional[ProductVariantRef], pydantic.Field(alias="productVariantRef")
    ] = None
    r"""Reference that links the line item to the specific version of product that has been ordered."""

    quantity: Annotated[
        Optional[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = None
    r"""Number of units of the product sold.
    For refunds, quantity is negative.

    """

    tax_percentage: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="taxPercentage"),
    ] = None
    r"""Percentage rate (from 0 to 100) of any sales tax applied to the unit price."""

    taxes: Optional[List[TaxComponentAllocation]] = None
    r"""Taxes breakdown as applied to order lines."""

    total_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalAmount"),
    ] = None
    r"""Total amount of the line item, including discounts and tax."""

    total_tax_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalTaxAmount"),
    ] = None
    r"""Total amount of tax applied to the line item, factoring in any discounts."""

    unit_price: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="unitPrice"),
    ] = None
    r"""Price per unit of goods or services, excluding discounts and tax."""
