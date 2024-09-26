"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountref import AccountRef, AccountRefTypedDict
from .accountspayabletracking import (
    AccountsPayableTracking,
    AccountsPayableTrackingTypedDict,
)
from .propertie_itemref import PropertieItemRef, PropertieItemRefTypedDict
from .taxrateref import TaxRateRef, TaxRateRefTypedDict
from .trackingcategoryref import TrackingCategoryRef, TrackingCategoryRefTypedDict
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
from enum import Enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class BillLineItemDataType(str, Enum):
    r"""Allowed name of the 'dataType'."""

    PURCHASE_ORDERS = "purchaseOrders"
    BILLS = "bills"


class RecordLineReferenceTypedDict(TypedDict):
    r"""Reference to the purchase order line this line was generated from."""

    data_type: NotRequired[BillLineItemDataType]
    r"""Allowed name of the 'dataType'."""
    id: NotRequired[str]
    r"""'id' of the underlying record."""
    line_number: NotRequired[str]
    r"""Line number of the underlying record."""


class RecordLineReference(BaseModel):
    r"""Reference to the purchase order line this line was generated from."""

    data_type: Annotated[
        Optional[BillLineItemDataType], pydantic.Field(alias="dataType")
    ] = None
    r"""Allowed name of the 'dataType'."""

    id: Optional[str] = None
    r"""'id' of the underlying record."""

    line_number: Annotated[Optional[str], pydantic.Field(alias="lineNumber")] = None
    r"""Line number of the underlying record."""


class BillLineItemTypedDict(TypedDict):
    quantity: Decimal
    r"""Number of units of goods or services received."""
    unit_amount: Decimal
    r"""Price of each unit of goods or services."""
    account_ref: NotRequired[AccountRefTypedDict]
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    description: NotRequired[Nullable[str]]
    r"""Friendly name of the goods or services received."""
    discount_amount: NotRequired[Nullable[Decimal]]
    r"""Numerical value of any discounts applied.

    Do not use to apply discounts in Oracle NetSuite—see Oracle NetSuite integration reference.
    """
    discount_percentage: NotRequired[Nullable[Decimal]]
    r"""Percentage rate of any discount applied to the bill."""
    is_direct_cost: NotRequired[bool]
    r"""The bill is a direct cost if `True`."""
    item_ref: NotRequired[PropertieItemRefTypedDict]
    r"""Reference to the item the line is linked to."""
    line_number: NotRequired[Nullable[str]]
    r"""The bill line's number."""
    purchase_order_line_ref: NotRequired[RecordLineReferenceTypedDict]
    sub_total: NotRequired[Nullable[Decimal]]
    r"""Amount of the line, inclusive of discounts but exclusive of tax."""
    tax_amount: NotRequired[Nullable[Decimal]]
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
    total_amount: NotRequired[Nullable[Decimal]]
    r"""Total amount of the line, including tax."""
    tracking: NotRequired[AccountsPayableTrackingTypedDict]
    r"""Categories, and a project and customer, against which the item is tracked."""
    tracking_category_refs: NotRequired[Nullable[List[TrackingCategoryRefTypedDict]]]
    r"""Collection of categories against which this item is tracked."""
    unit_of_measurement: NotRequired[Nullable[str]]
    r"""The measurement which defines a unit for this item (e.g. 'kilogram', 'litre')."""


class BillLineItem(BaseModel):
    quantity: Annotated[
        Decimal,
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ]
    r"""Number of units of goods or services received."""

    unit_amount: Annotated[
        Annotated[
            Decimal,
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="unitAmount"),
    ]
    r"""Price of each unit of goods or services."""

    account_ref: Annotated[Optional[AccountRef], pydantic.Field(alias="accountRef")] = (
        None
    )
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""

    description: OptionalNullable[str] = UNSET
    r"""Friendly name of the goods or services received."""

    discount_amount: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="discountAmount"),
    ] = UNSET
    r"""Numerical value of any discounts applied.

    Do not use to apply discounts in Oracle NetSuite—see Oracle NetSuite integration reference.
    """

    discount_percentage: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="discountPercentage"),
    ] = UNSET
    r"""Percentage rate of any discount applied to the bill."""

    is_direct_cost: Annotated[Optional[bool], pydantic.Field(alias="isDirectCost")] = (
        None
    )
    r"""The bill is a direct cost if `True`."""

    item_ref: Annotated[Optional[PropertieItemRef], pydantic.Field(alias="itemRef")] = (
        None
    )
    r"""Reference to the item the line is linked to."""

    line_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="lineNumber")
    ] = UNSET
    r"""The bill line's number."""

    purchase_order_line_ref: Annotated[
        Optional[RecordLineReference], pydantic.Field(alias="purchaseOrderLineRef")
    ] = None

    sub_total: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="subTotal"),
    ] = UNSET
    r"""Amount of the line, inclusive of discounts but exclusive of tax."""

    tax_amount: Annotated[
        Annotated[
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="taxAmount"),
    ] = UNSET
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
            OptionalNullable[Decimal],
            BeforeValidator(validate_decimal),
            PlainSerializer(serialize_decimal(False)),
        ],
        pydantic.Field(alias="totalAmount"),
    ] = UNSET
    r"""Total amount of the line, including tax."""

    tracking: Optional[AccountsPayableTracking] = None
    r"""Categories, and a project and customer, against which the item is tracked."""

    tracking_category_refs: Annotated[
        OptionalNullable[List[TrackingCategoryRef]],
        pydantic.Field(alias="trackingCategoryRefs"),
    ] = UNSET
    r"""Collection of categories against which this item is tracked."""

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
            "isDirectCost",
            "itemRef",
            "lineNumber",
            "purchaseOrderLineRef",
            "subTotal",
            "taxAmount",
            "taxRateRef",
            "totalAmount",
            "tracking",
            "trackingCategoryRefs",
            "unitOfMeasurement",
        ]
        nullable_fields = [
            "description",
            "discountAmount",
            "discountPercentage",
            "lineNumber",
            "subTotal",
            "taxAmount",
            "totalAmount",
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
