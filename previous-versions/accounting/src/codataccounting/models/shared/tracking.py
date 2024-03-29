"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .invoiceto import InvoiceTo
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RecordReference:
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType'), 'exclude': lambda f: f is None }})
    r"""Allowed name of the 'dataType'."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""'id' of the underlying record or data type."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Tracking:
    record_refs: List[InvoiceTo] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRefs') }})
    invoice_to: Optional[RecordReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoiceTo'), 'exclude': lambda f: f is None }})
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    

