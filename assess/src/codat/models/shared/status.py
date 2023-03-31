"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dataintegritystatus as shared_dataintegritystatus
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Status:
    r"""OK"""
    
    metadata: Optional[list[shared_dataintegritystatus.DataIntegrityStatus]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})  
    