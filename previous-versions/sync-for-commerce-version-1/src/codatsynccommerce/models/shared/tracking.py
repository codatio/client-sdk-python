"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountingcustomerref as shared_accountingcustomerref
from ..shared import billedtotype as shared_billedtotype
from ..shared import recordref as shared_recordref
from ..shared import trackingcategoryrefsitems as shared_trackingcategoryrefsitems
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TrackingProjectReference:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier to the project reference."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The project's name."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Tracking:
    r"""Categories, and a project and customer, against which the item is tracked."""
    category_refs: list[shared_trackingcategoryrefsitems.TrackingCategoryRefsitems] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryRefs') }})
    is_billed_to: shared_billedtotype.BilledToType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBilledTo') }})
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    is_rebilled_to: shared_billedtotype.BilledToType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRebilledTo') }})
    r"""Defines if the bill or bill credit note is billed/rebilled to a project."""
    customer_ref: Optional[shared_accountingcustomerref.AccountingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[TrackingProjectReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectRef'), 'exclude': lambda f: f is None }})
    record_ref: Optional[shared_recordref.RecordRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})
    r"""Links the current record to the underlying record or data type that created it.

    For example, if a journal entry is generated based on an invoice, this property allows you to connect the journal entry to the underlying invoice in our data model.
    """
    

