"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import expensetransaction as shared_expensetransaction
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateExpenseRequest:
    
    items: Optional[list[shared_expensetransaction.ExpenseTransaction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    