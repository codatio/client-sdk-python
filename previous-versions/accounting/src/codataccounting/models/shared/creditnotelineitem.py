"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountingcustomerref as shared_accountingcustomerref
from ..shared import accountref as shared_accountref
from ..shared import billedtotype1 as shared_billedtotype1
from ..shared import invoiceto as shared_invoiceto
from ..shared import itemref as shared_itemref
from ..shared import projectref as shared_projectref
from ..shared import taxrateref as shared_taxrateref
from ..shared import trackingcategoryref as shared_trackingcategoryref
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreditNoteLineItemTracking:
    r"""Categories, and a project and customer, against which the item is tracked."""
    category_refs: list[shared_trackingcategoryref.TrackingCategoryRef] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryRefs') }})
    is_billed_to: shared_billedtotype1.BilledToType1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBilledTo') }})
    is_rebilled_to: shared_billedtotype1.BilledToType1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRebilledTo') }})
    customer_ref: Optional[shared_accountingcustomerref.AccountingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[shared_projectref.ProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectRef'), 'exclude': lambda f: f is None }})
    record_ref: Optional[shared_invoiceto.InvoiceTo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreditNoteLineItem:
    quantity: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quantity') }})
    r"""Number of units of the goods or service for which credit has been issued."""
    unit_amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unitAmount') }})
    r"""Unit price of the goods or service."""
    account_ref: Optional[shared_accountref.AccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""Friendly name of each line item. For example, the goods or service for which credit has been issued."""
    discount_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountAmount'), 'exclude': lambda f: f is None }})
    r"""Value of any discounts applied."""
    discount_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('discountPercentage'), 'exclude': lambda f: f is None }})
    r"""Percentage rate of any discount applied to the line item."""
    is_direct_income: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isDirectIncome'), 'exclude': lambda f: f is None }})
    item_ref: Optional[shared_itemref.ItemRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemRef'), 'exclude': lambda f: f is None }})
    sub_total: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subTotal'), 'exclude': lambda f: f is None }})
    r"""Amount of credit associated with the line item, including discounts but excluding tax."""
    tax_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'exclude': lambda f: f is None }})
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
    total_amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'exclude': lambda f: f is None }})
    r"""Total amount of the line item, including discounts and tax."""
    tracking: Optional[CreditNoteLineItemTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})
    r"""Categories, and a project and customer, against which the item is tracked."""
    tracking_category_refs: Optional[list[shared_trackingcategoryref.TrackingCategoryRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingCategoryRefs'), 'exclude': lambda f: f is None }})
    r"""Reference to the tracking categories to which the line item is linked.

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    

