"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatbankfeeds import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BankFeedAccountMappingResponse:
    r"""The result from POSTing a Bank Account mapping."""
    UNSET='__SPEAKEASY_UNSET__'
    error: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Error'), 'exclude': lambda f: f is BankFeedAccountMappingResponse.UNSET }})
    r"""Error returned during the post request"""
    status: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Status'), 'exclude': lambda f: f is BankFeedAccountMappingResponse.UNSET }})
    r"""Status of the POST request."""
    source_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceAccountId'), 'exclude': lambda f: f is None }})
    r"""Unique ID for the source account."""
    target_account_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('targetAccountId'), 'exclude': lambda f: f is BankFeedAccountMappingResponse.UNSET }})
    r"""Unique ID for the target account."""
    

