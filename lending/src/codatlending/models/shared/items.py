"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Items:
    amount: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Amount of tax withheld."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name assigned to withheld tax."""
    

