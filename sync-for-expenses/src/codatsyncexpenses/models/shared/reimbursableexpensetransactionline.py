"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .invoiceto import InvoiceTo
from .recordref import RecordRef
from .trackingref import TrackingRef
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReimbursableExpenseTransactionLine:
    UNSET='__SPEAKEASY_UNSET__'
    account_ref: RecordRef = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef') }})
    net_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of the line, exclusive of tax."""
    invoice_to: Optional[InvoiceTo] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTo'), 'exclude': lambda f: f is ReimbursableExpenseTransactionLine.UNSET }})
    r"""Unique identifier of the customer the expense is billable to. The invoiceTo object is currently only supported for QBO."""
    tax_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Amount of tax for the line."""
    tax_rate_ref: Optional[RecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxRateRef'), 'exclude': lambda f: f is None }})
    tracking_refs: Optional[List[TrackingRef]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trackingRefs'), 'exclude': lambda f: f is ReimbursableExpenseTransactionLine.UNSET }})
    

