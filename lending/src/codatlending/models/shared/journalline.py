"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountref as shared_accountref
from ..shared import recordref as shared_recordref
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class JournalLineTracking:
    r"""List of record refs associated with the tracking information for the line (eg to a Tracking Category, or customer etc.)"""
    record_refs: Optional[list[shared_recordref.RecordRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRefs') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class JournalLine:
    net_amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('netAmount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Amount for the journal line. Debit entries are considered positive, and credit entries are considered negative."""
    account_ref: Optional[shared_accountref.AccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})
    r"""Data types that reference an account, for example bill and invoice line items, use an accountRef that includes the ID and name of the linked account."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""Currency for the journal line item."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Description of the journal line item."""
    tracking: Optional[JournalLineTracking] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tracking'), 'exclude': lambda f: f is None }})
    r"""List of record refs associated with the tracking information for the line (eg to a Tracking Category, or customer etc.)"""
    

