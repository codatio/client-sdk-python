"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountref as shared_accountref
from ..shared import itemref as shared_itemref
from ..shared import propertiestracking as shared_propertiestracking
from ..shared import taxrateref as shared_taxrateref
from ..shared import trackingcategoryref as shared_trackingcategoryref
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from enum import Enum
from typing import Optional

class BillLineItemRecordLineReferenceDataType(str, Enum):
    r"""Allowed name of the 'dataType'."""
    PURCHASE_ORDERS = 'purchaseOrders'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BillLineItemRecordLineReference:
    r"""Reference to the purchase order line this line was generated from."""
    data_type: Optional[BillLineItemRecordLineReferenceDataType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Allowed name of the 'dataType'."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' of the underlying record."""
    line_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineNumber'), 'exclude': lambda f: f is None }})
    r"""Line number of the underlying record."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BillLineItem:
    quantity: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Number of units of goods or services received."""
    unit_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Price of each unit of goods or services."""
    account_ref: Optional[shared_accountref.AccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Friendly name of the goods or services received."""
    discount_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Numerical value of any discounts applied.

    Do not use to apply discounts in Oracle NetSuite—see Oracle NetSuite integration reference.
    """
    discount_percentage: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Percentage rate of any discount applied to the bill."""
    is_direct_cost: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDirectCost'), 'exclude': lambda f: f is None }})
    r"""The bill is a direct cost if `True`."""
    item_ref: Optional[shared_itemref.ItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})
    line_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lineNumber') }})
    r"""The bill line's number."""
    purchase_order_line_ref: Optional[BillLineItemRecordLineReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purchaseOrderLineRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the purchase order line this line was generated from."""
    sub_total: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of the line, inclusive of discounts but exclusive of tax."""
    tax_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of tax for the line."""
    tax_rate_ref: Optional[shared_taxrateref.TaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference a tax rate, for example invoice and bill line items, use a taxRateRef that includes the ID and name of the linked tax rate.

    Found on:

    - Bill line items
    - Bill Credit Note line items
    - Credit Note line items
    - Direct incomes line items
    - Invoice line items
    - Items
    """
    total_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Total amount of the line, including tax."""
    tracking: Optional[shared_propertiestracking.Propertiestracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})
    r"""Categories, and a project and customer, against which the item is tracked."""
    tracking_category_refs: Optional[list[shared_trackingcategoryref.TrackingCategoryRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingCategoryRefs') }})
    r"""Collection of categories against which this item is tracked."""
    

