"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import billedtotype as shared_billedtotype
from ..shared import trackingcategoryref as shared_trackingcategoryref
from codatsyncpayables import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TrackingCustomerRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""`id` from the Customers data type"""
    company_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyName'), 'exclude': lambda f: f is None }})
    r"""`customerName` from the Customer data type"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TrackingProjectRef:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Tracking:
    r"""Categories, and a project and customer, against which the item is tracked."""
    category_refs: list[shared_trackingcategoryref.TrackingCategoryRef] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categoryRefs') }})
    is_billed_to: shared_billedtotype.BilledToType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isBilledTo') }})
    is_rebilled_to: shared_billedtotype.BilledToType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isRebilledTo') }})
    customer_ref: Optional[TrackingCustomerRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerRef'), 'exclude': lambda f: f is None }})
    project_ref: Optional[TrackingProjectRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projectRef'), 'exclude': lambda f: f is None }})
    
