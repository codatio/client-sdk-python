"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TaxRateComponent:
    r"""A tax rate can be made up of multiple sub taxes, often called components of the tax."""
    
    is_compound: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isCompound') }})
    r"""A flag to indicate with the tax is calculated using the principle of compounding."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the tax rate component."""
    rate: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rate'), 'exclude': lambda f: f is None }})
    r"""The rate of the tax rate component, usually a percentage."""
    