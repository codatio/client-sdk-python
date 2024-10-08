"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountref import AccountRef, AccountRefTypedDict
from .itemref import ItemRef, ItemRefTypedDict
from .taxrateref import TaxRateRef, TaxRateRefTypedDict
from .trackingcategoryref import TrackingCategoryRef, TrackingCategoryRefTypedDict
from codat_accounting.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_accounting.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class PurchaseOrderLineItemTypedDict(TypedDict):
    account_ref: NotRequired[AccountRefTypedDict]
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    description: NotRequired[Nullable[str]]
    r"""Description of the goods / services that have been ordered."""
    discount_amount: NotRequired[Decimal]
    r"""Value of any discounts applied."""
    discount_percentage: NotRequired[Decimal]
    r"""Percentage rate (from 0 to 100) of any discounts applied to the unit amount."""
    item_ref: NotRequired[ItemRefTypedDict]
    line_number: NotRequired[Nullable[str]]
    r"""The purchase order line's number."""
    quantity: NotRequired[Decimal]
    r"""Number of units that have been ordered."""
    sub_total: NotRequired[Decimal]
    r"""Amount of the line, inclusive of discounts but exclusive of tax."""
    tax_amount: NotRequired[Decimal]
    r"""Amount of tax for the line."""
    tax_rate_ref: NotRequired[TaxRateRefTypedDict]
    r"""Data types that reference a tax rate, for example invoice and bill line items, use a taxRateRef that includes the ID and name of the linked tax rate.

    Found on:

    - Bill line items
    - Bill Credit Note line items
    - Credit Note line items
    - Direct incomes line items
    - Invoice line items
    - Items
    """
    total_amount: NotRequired[Decimal]
    r"""Total amount of the line, inclusive of discounts and tax."""
    tracking_category_refs: NotRequired[Nullable[List[TrackingCategoryRefTypedDict]]]
    r"""Reference to the tracking categories to which the line item is linked."""
    unit_amount: NotRequired[Decimal]
    r"""Price of each unit."""
    unit_of_measurement: NotRequired[Nullable[str]]
    r"""The measurement which defines a unit for this item (e.g. 'kilogram', 'litre')."""


class PurchaseOrderLineItem(BaseModel):
    account_ref: Annotated[Optional[AccountRef], pydantic.Field(alias="accountRef")] = (
        None
    )
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""

    description: OptionalNullable[str] = UNSET
    r"""Description of the goods / services that have been ordered."""

    discount_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="discountAmount"),
    ] = None
    r"""Value of any discounts applied."""

    discount_percentage: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="discountPercentage"),
    ] = None
    r"""Percentage rate (from 0 to 100) of any discounts applied to the unit amount."""

    item_ref: Annotated[Optional[ItemRef], pydantic.Field(alias="itemRef")] = None

    line_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="lineNumber")
    ] = UNSET
    r"""The purchase order line's number."""

    quantity: Annotated[
        Optional[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = None
    r"""Number of units that have been ordered."""

    sub_total: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="subTotal"),
    ] = None
    r"""Amount of the line, inclusive of discounts but exclusive of tax."""

    tax_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="taxAmount"),
    ] = None
    r"""Amount of tax for the line."""

    tax_rate_ref: Annotated[
        Optional[TaxRateRef], pydantic.Field(alias="taxRateRef")
    ] = None
    r"""Data types that reference a tax rate, for example invoice and bill line items, use a taxRateRef that includes the ID and name of the linked tax rate.

    Found on:

    - Bill line items
    - Bill Credit Note line items
    - Credit Note line items
    - Direct incomes line items
    - Invoice line items
    - Items
    """

    total_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalAmount"),
    ] = None
    r"""Total amount of the line, inclusive of discounts and tax."""

    tracking_category_refs: Annotated[
        OptionalNullable[List[TrackingCategoryRef]],
        pydantic.Field(alias="trackingCategoryRefs"),
    ] = UNSET
    r"""Reference to the tracking categories to which the line item is linked."""

    unit_amount: Annotated[
        Annotated[
            Optional[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="unitAmount"),
    ] = None
    r"""Price of each unit."""

    unit_of_measurement: Annotated[
        OptionalNullable[str], pydantic.Field(alias="unitOfMeasurement")
    ] = UNSET
    r"""The measurement which defines a unit for this item (e.g. 'kilogram', 'litre')."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "accountRef",
            "description",
            "discountAmount",
            "discountPercentage",
            "itemRef",
            "lineNumber",
            "quantity",
            "subTotal",
            "taxAmount",
            "taxRateRef",
            "totalAmount",
            "trackingCategoryRefs",
            "unitAmount",
            "unitOfMeasurement",
        ]
        nullable_fields = [
            "description",
            "lineNumber",
            "trackingCategoryRefs",
            "unitOfMeasurement",
        ]
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
