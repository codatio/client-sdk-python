"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .configaccount import ConfigAccount
from .feessupplier import FeesSupplier
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Fees:
    accounts: Optional[Dict[str, ConfigAccount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts') }})
    fees_supplier: Optional[FeesSupplier] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feesSupplier'), 'exclude': lambda f: f is None }})
    sync_fees: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncFees'), 'exclude': lambda f: f is None }})
    r"""Boolean indicator to enable syncing fees."""
    

