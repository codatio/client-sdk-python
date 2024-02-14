"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatsyncpayroll import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PushFieldValidation:
    UNSET='__SPEAKEASY_UNSET__'
    details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('details') }})
    r"""Details on the validation issue."""
    field: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field'), 'exclude': lambda f: f is None }})
    r"""Field name that resulted in the validation issue."""
    ref: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref'), 'exclude': lambda f: f is PushFieldValidation.UNSET }})
    r"""Unique reference identifier for the validation issue."""
    

