"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountingcustomerref import AccountingCustomerRef
from .accountref import AccountRef
from .billedtotype1 import BilledToType1
from .invoiceto import InvoiceTo
from .itemref import ItemRef
from .projectref import ProjectRef
from .taxrateref import TaxRateRef
from .trackingcategoryref import TrackingCategoryRef
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditNoteLineItemTracking:
    r"""Categories, and a project and customer, against which the item is tracked."""
    category_refs: List[TrackingCategoryRef] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryRefs') }})
    is_billed_to: BilledToType1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBilledTo') }})
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    is_rebilled_to: BilledToType1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRebilledTo') }})
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    customer_ref: Optional[AccountingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[ProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectRef'), 'exclude': lambda f: f is None }})
    record_ref: Optional[InvoiceTo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreditNoteLineItem:
    quantity: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Number of units of the goods or service for which credit has been issued."""
    unit_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Unit price of the goods or service."""
    account_ref: Optional[AccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Friendly name of each line item. For example, the goods or service for which credit has been issued."""
    discount_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Value of any discounts applied."""
    discount_percentage: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Percentage rate of any discount applied to the line item."""
    is_direct_income: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDirectIncome'), 'exclude': lambda f: f is None }})
    r"""The credit note is a direct income if `True`."""
    item_ref: Optional[ItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})
    sub_total: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of credit associated with the line item, including discounts but excluding tax."""
    tax_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of tax associated with the line item."""
    tax_rate_ref: Optional[TaxRateRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateRef'), 'exclude': lambda f: f is None }})
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
    tracking: Optional[CreditNoteLineItemTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})
    r"""Categories, and a project and customer, against which the item is tracked."""
    tracking_category_refs: Optional[List[TrackingCategoryRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingCategoryRefs') }})
    r"""Reference to the tracking categories to which the line item is linked.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    

