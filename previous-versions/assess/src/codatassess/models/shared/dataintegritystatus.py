"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .dataintegrityamounts import DataIntegrityAmounts
from .dataintegrityconnectionid import DataIntegrityConnectionID
from .dataintegritydates import DataIntegrityDates
from .dataintegritystatusinfo import DataIntegrityStatusInfo
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DataIntegrityStatus:
    amounts: Optional[DataIntegrityAmounts] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amounts'), 'exclude': lambda f: f is None }})
    r"""Only returned for transactions. For accounts, there is nothing returned."""
    connection_ids: Optional[DataIntegrityConnectionID] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionIds'), 'exclude': lambda f: f is None }})
    dates: Optional[DataIntegrityDates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dates'), 'exclude': lambda f: f is None }})
    r"""Only returned for transactions. For accounts, there is nothing returned."""
    status_info: Optional[DataIntegrityStatusInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusInfo'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The data type which the data type in the URL has been matched against. For example, if you've matched accountTransactions and banking-transactions, and you call this endpoint with accountTransactions in the URL, this property would be banking-transactions."""
    

