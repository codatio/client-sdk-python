"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .reportline import ReportLine
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from decimal import Decimal
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReportLineInput:
    value: Decimal = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'encoder': utils.decimalencoder(False, False), 'decoder': utils.decimaldecoder }})
    r"""Numerical value of the line item."""
    account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountId') }})
    r"""Identifier for the account, unique for the company in the accounting platform."""
    items: Optional[List[ReportLine]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""An array of ReportLine items."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the report line item."""
    

