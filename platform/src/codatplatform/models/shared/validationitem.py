"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatplatform import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ValidationItem:
    UNSET='__SPEAKEASY_UNSET__'
    item_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('itemId'), 'exclude': lambda f: f is ValidationItem.UNSET }})
    r"""Unique identifier for a validation item."""
    message: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is ValidationItem.UNSET }})
    r"""A message outlining validation item's issue."""
    validator_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validatorName'), 'exclude': lambda f: f is ValidationItem.UNSET }})
    r"""Name of validator."""
    

