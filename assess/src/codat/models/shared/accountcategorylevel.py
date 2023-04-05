"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountCategoryLevel:
    r"""An object containing an ordered list of account category levels."""
    
    confidence: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidence'), 'exclude': lambda f: f is None }})
    r"""Confidence level of the category. This will only be populated where `status` is `Suggested`."""  
    level_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('levelName'), 'exclude': lambda f: f is None }})
    r"""Account category name."""  
    