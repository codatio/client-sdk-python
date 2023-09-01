"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import halref as shared_halref
from codatsyncpayroll import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Links:
    current: shared_halref.HalRef = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})
    self_: shared_halref.HalRef = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self') }})
    next: Optional[shared_halref.HalRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[shared_halref.HalRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})
    
