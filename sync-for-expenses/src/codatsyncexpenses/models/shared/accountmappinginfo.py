"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional

class AccountMappingInfoAccountType(str, Enum):
    r"""Type of the account."""
    ASSET = 'Asset'
    LIABILITY = 'Liability'
    INCOME = 'Income'
    EXPENSE = 'Expense'
    EQUITY = 'Equity'

class ValidTransactionTypes(str, Enum):
    PAYMENT = 'Payment'
    REFUND = 'Refund'
    REWARD = 'Reward'
    CHARGEBACK = 'Chargeback'
    TRANSFER_IN = 'TransferIn'
    TRANSFER_OUT = 'TransferOut'
    ADJUSTMENT_IN = 'AdjustmentIn'
    ADJUSTMENT_OUT = 'AdjustmentOut'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountMappingInfo:
    account_type: Optional[AccountMappingInfoAccountType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountType') }})
    r"""Type of the account."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""Currency of the account."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier of account."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the account as it appears in the companies accounting software."""
    valid_transaction_types: Optional[List[ValidTransactionTypes]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validTransactionTypes') }})
    r"""Supported transaction types for the account."""
    

