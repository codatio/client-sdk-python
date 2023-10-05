"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountbalanceamounts as shared_accountbalanceamounts
from ..shared import accountidentifiers as shared_accountidentifiers
from ..shared import accountinstitution as shared_accountinstitution
from ..shared import accounttype as shared_accounttype
from codatbanking import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Account:
    r"""This data type provides a list of all the SMB's bank accounts, with rich data like balances, account numbers, and institutions holding the accounts.

    Explore our [data coverage](https://knowledge.codat.io/supported-features/banking?view=tab-by-data-type&dataType=banking-accounts).

    Responses are paged, so you should provide `page` and `pageSize` query parameters in your request.
    """
    balance: shared_accountbalanceamounts.AccountBalanceAmounts = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('balance') }})
    r"""Depending on the data provided by the underlying bank, not all balances are always available."""
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""The currency code for the account."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The ID of the account from the provider."""
    identifiers: shared_accountidentifiers.AccountIdentifiers = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('identifiers') }})
    r"""An object containing bank account identification information."""
    institution: shared_accountinstitution.AccountInstitution = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('institution') }})
    r"""The bank or other financial institution providing the account."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the account according to the provider."""
    type: shared_accounttype.AccountType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of transactions and balances on the account.
    For Credit accounts, positive balances are liabilities, and positive transactions **reduce** liabilities.  
    For Debit accounts, positive balances are assets, and positive transactions **increase** assets.
    """
    holder: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('holder') }})
    r"""The name of the person or company who holds the account."""
    informal_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('informalName') }})
    r"""The friendly name of the account, chosen by the holder. This may not have been set by the account holder and therefore is not always available."""
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    

