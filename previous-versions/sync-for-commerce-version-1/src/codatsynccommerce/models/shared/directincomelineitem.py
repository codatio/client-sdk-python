"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountref as shared_accountref
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DirectIncomeLineItemItemReference:
    r"""Reference to the product, service type, or inventory item to which the direct cost is linked."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier for the item in the accounting platform."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the item in the accounting platform."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DirectIncomeLineItemTaxRateReference:
    r"""Reference to the tax rate to which the line item is linked."""
    effective_tax_rate: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('effectiveTaxRate'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Applicable tax rate."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the tax rate in the accounting platform."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the tax rate in the accounting platform."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DirectIncomeLineItemTrackingCategoryRefs:
    r"""References a category against which the item is tracked.

    Deprecated class: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier to the tracking category."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of tracking category."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DirectIncomeLineItem:
    quantity: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""The number of units of goods or services received.

    Note: If the platform does not provide this information, the quantity will be mapped as 1.
    """
    unit_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""The price of each unit of goods or services.
    Note: If the platform does not provide this information, the unit amount will be mapped to the total amount.
    """
    account_ref: Optional[shared_accountref.AccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""A user-friendly name of the goods or services."""
    discount_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Discount amount for the line before tax."""
    discount_percentage: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Discount percentage for the line before tax."""
    item_ref: Optional[DirectIncomeLineItemItemReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the product, service type, or inventory item to which the direct cost is linked."""
    sub_total: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""The amount of the line, inclusive of discounts, but exclusive of tax."""
    tax_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""The amount of tax for the line.
    Note: If the platform does not provide this information, the quantity will be mapped as 0.00.
    """
    tax_rate_ref: Optional[DirectIncomeLineItemTaxRateReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the tax rate to which the line item is linked."""
    total_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""The total amount of the line, including tax."""
    tracking_category_refs: Optional[list[DirectIncomeLineItemTrackingCategoryRefs]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingCategoryRefs') }})
    r"""An array of categories against which this direct cost is tracked."""
    

