"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dataintegritysummary as shared_dataintegritysummary
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Summaries:
    r"""OK"""
    
    summaries: Optional[list[shared_dataintegritysummary.DataIntegritySummary]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summaries'), 'exclude': lambda f: f is None }})  
    