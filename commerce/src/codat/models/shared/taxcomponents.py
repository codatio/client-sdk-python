"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import taxcomponent as shared_taxcomponent
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxComponents:
    r"""OK"""
    
    tax_components: Optional[list[shared_taxcomponent.TaxComponent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('taxComponents'), 'exclude': lambda f: f is None }})  
    