"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AccountBalance:
    available: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('available'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""The account's current balance"""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""The currency of the account"""
    pending: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pending'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""Funds that are not yet available in the balance"""
    reserved: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reserved'), 'exclude': lambda f: f is None }})
    r"""Funds reserved as holdings"""
    

