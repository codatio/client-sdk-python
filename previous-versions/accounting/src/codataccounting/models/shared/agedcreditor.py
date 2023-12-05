"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .agedoutstandingamount import AgedOutstandingAmount
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountingAgedCurrencyOutstanding:
    aged_outstanding_amounts: Optional[List[AgedOutstandingAmount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agedOutstandingAmounts'), 'exclude': lambda f: f is None }})
    r"""Array of outstanding amounts by period."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction. 

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AgedCreditor:
    aged_currency_outstanding: Optional[List[AccountingAgedCurrencyOutstanding]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agedCurrencyOutstanding'), 'exclude': lambda f: f is None }})
    r"""Array of aged creditors by currency."""
    supplier_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplierId'), 'exclude': lambda f: f is None }})
    r"""Supplier ID of the aged creditor."""
    supplier_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supplierName'), 'exclude': lambda f: f is None }})
    r"""Supplier name of the aged creditor."""
    

