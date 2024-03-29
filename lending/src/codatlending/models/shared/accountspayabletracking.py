"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .accountingcustomerref import AccountingCustomerRef
from .billedtotype import BilledToType
from .projectref import ProjectRef
from .trackingcategoryref import TrackingCategoryRef
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountsPayableTracking:
    r"""Categories, and a project and customer, against which the item is tracked."""
    category_refs: List[TrackingCategoryRef] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryRefs') }})
    is_billed_to: BilledToType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBilledTo') }})
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    is_rebilled_to: BilledToType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRebilledTo') }})
    r"""Defines if the invoice or credit note is billed/rebilled to a project or customer."""
    customer_ref: Optional[AccountingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[ProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectRef'), 'exclude': lambda f: f is None }})
    

