"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SupplierRef:
    r"""Reference to the supplier the record relates to."""
    UNSET='__SPEAKEASY_UNSET__'
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The supplier's unique ID"""
    supplier_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplierName'), 'exclude': lambda f: f is SupplierRef.UNSET }})
    r"""The supplier's name"""
    

