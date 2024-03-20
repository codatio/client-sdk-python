"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .bill import Bill
from codatsyncpayables import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BillEventPayload:
    UNSET='__SPEAKEASY_UNSET__'
    bill: Optional[Bill] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bill'), 'exclude': lambda f: f is BillEventPayload.UNSET }})
    r"""Bills are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services."""
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for your SMB in Codat."""
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for a company's data connection."""
    push_operation_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pushOperationKey'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the push operation."""
    
