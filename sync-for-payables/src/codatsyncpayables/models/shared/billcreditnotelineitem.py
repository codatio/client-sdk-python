"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountref as shared_accountref
from ..shared import billedtotype as shared_billedtotype
from ..shared import taxrateref as shared_taxrateref
from ..shared import trackingcategoryref as shared_trackingcategoryref
from codatsyncpayables import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BillCreditNoteLineItemItemReference:
    r"""Reference to the item the line is linked to."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier for the item in the accounting platform."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the item in the accounting platform."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BillCreditNoteLineItemTrackingCustomerRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""`id` from the Customers data type"""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyName') }})
    r"""`customerName` from the Customer data type"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BillCreditNoteLineItemTrackingProjectReference:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier to the project reference."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The project's name."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BillCreditNoteLineItemTracking:
    r"""Categories, and a project and customer, against which the item is tracked."""
    category_refs: list[shared_trackingcategoryref.TrackingCategoryRef] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryRefs') }})
    is_billed_to: shared_billedtotype.BilledToType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBilledTo') }})
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    is_rebilled_to: shared_billedtotype.BilledToType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRebilledTo') }})
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    customer_ref: Optional[BillCreditNoteLineItemTrackingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[BillCreditNoteLineItemTrackingProjectReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectRef'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BillCreditNoteLineItem:
    quantity: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Number of units of the goods or service for which credit has been received."""
    unit_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Unit price of the goods or service."""
    account_ref: Optional[shared_accountref.AccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Friendly name of each line item. For example, the goods or service for which credit has been received."""
    discount_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Value of any discounts applied."""
    discount_percentage: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Percentage rate of any discount applied to the line item."""
    item_ref: Optional[BillCreditNoteLineItemItemReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})
    r"""Reference to the item the line is linked to."""
    sub_total: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of credit associated with the line item, including discounts but excluding tax."""
    tax_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of tax associated with the line item."""
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
    r"""Total amount of the line item, including discounts and tax."""
    tracking: Optional[BillCreditNoteLineItemTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})
    r"""Categories, and a project and customer, against which the item is tracked."""
    tracking_category_refs: Optional[list[shared_trackingcategoryref.TrackingCategoryRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingCategoryRefs') }})
    r"""Reference to the tracking categories to which the line item is linked.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    

