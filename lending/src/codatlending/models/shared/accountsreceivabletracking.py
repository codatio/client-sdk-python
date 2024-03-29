"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountingcustomerref import AccountingCustomerRef
from .billedtotype1 import BilledToType1
from .projectref import ProjectRef
from .trackingcategoryref import TrackingCategoryRef
from codatlending import utils
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
class AccountsReceivableTracking:
    r"""Categories, and a project and customer, against which the item is tracked."""
    category_refs: List[TrackingCategoryRef] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryRefs') }})
    is_billed_to: BilledToType1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBilledTo') }})
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    is_rebilled_to: BilledToType1 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRebilledTo') }})
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    customer_ref: Optional[AccountingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[ProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectRef'), 'exclude': lambda f: f is None }})
    record_ref: Optional[RecordReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    

