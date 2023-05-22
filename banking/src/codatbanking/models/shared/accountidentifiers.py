"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountidentifiertype as shared_accountidentifiertype
from codatbanking import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountIdentifiers:
    r"""An object containing bank account identification information."""
    
    type: shared_accountidentifiertype.AccountIdentifierType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""Type of account"""
    bank_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bankCode'), 'exclude': lambda f: f is None }})
    r"""The local (usually national) routing number for the account.
    
    This is known by different names in different countries:
    * BSB code (Australia)
    * routing number (Canada, USA)
    * sort code (UK)
    """
    bic: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bic'), 'exclude': lambda f: f is None }})
    r"""The ISO 9362 code (commonly called SWIFT code, SWIFT-BIC or BIC) for the account."""
    iban: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('iban'), 'exclude': lambda f: f is None }})
    r"""The international bank account number (IBAN) for the account, if known."""
    masked_account_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maskedAccountNumber'), 'exclude': lambda f: f is None }})
    r"""A portion of the actual account `number` to help account identification where number is tokenised (Plaid only)"""
    number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('number'), 'exclude': lambda f: f is None }})
    r"""The account number for the account. When combined with the`bankCode`, this is usually enough to uniquely identify an account within a jurisdiction."""
    subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtype'), 'exclude': lambda f: f is None }})
    r"""Detailed account category"""
    