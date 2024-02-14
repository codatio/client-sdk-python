"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountBalanceAmounts:
    r"""Depending on the data provided by the underlying bank, not all balances are always available."""
    UNSET='__SPEAKEASY_UNSET__'
    available: Optional[Decimal] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('available'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is AccountBalanceAmounts.UNSET }})
    r"""The balance available in the account, including any pending transactions. This doesn't include additional funds available from any overdrafts."""
    current: Optional[Decimal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is None }})
    r"""The balance of the account only including cleared transactions."""
    limit: Optional[Decimal] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'encoder': utils.decimalencoder(True, False), 'decoder': utils.decimaldecoder, 'exclude': lambda f: f is AccountBalanceAmounts.UNSET }})
    r"""The minimum allowed balance for the account. For example, a $100.00 overdraft would show as a limit of `-100.00`."""
    

