"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatcommerce import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrderDiscountAllocation:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the discount in the commerce or point of sale platform."""
    total_amount: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalAmount'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Total amount of discount applied."""
    

