"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .halref import HalRef
from codatsyncpayables import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Links:
    current: HalRef = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current') }})
    self_: HalRef = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self') }})
    next: Optional[HalRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[HalRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous'), 'exclude': lambda f: f is None }})
    

