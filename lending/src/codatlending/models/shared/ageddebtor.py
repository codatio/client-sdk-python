"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import agedcurrencyoutstanding as shared_agedcurrencyoutstanding
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AgedDebtor:
    aged_currency_outstanding: Optional[list[shared_agedcurrencyoutstanding.AgedCurrencyOutstanding]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agedCurrencyOutstanding'), 'exclude': lambda f: f is None }})
    r"""Array of aged debtors by currency."""
    customer_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerId'), 'exclude': lambda f: f is None }})
    r"""Customer ID of the aged debtor."""
    customer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerName'), 'exclude': lambda f: f is None }})
    r"""Customer name of the aged debtor."""
    

