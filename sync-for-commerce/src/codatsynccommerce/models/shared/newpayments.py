"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .configaccount import ConfigAccount
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewPayments:
    UNSET='__SPEAKEASY_UNSET__'
    accounts: Optional[Dict[str, ConfigAccount]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts'), 'exclude': lambda f: f is NewPayments.UNSET }})
    sync_payments: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncPayments'), 'exclude': lambda f: f is None }})
    r"""Boolean indicator for syncing payments."""
    

