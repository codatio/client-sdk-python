"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import transactioncategorystatus as shared_transactioncategorystatus
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BankingTransactionCategory:
    r"""Status of the bank transaction category."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique identifier of the bank transaction category."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the bank transaction category."""
    has_children: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasChildren'), 'exclude': lambda f: f is None }})
    r"""A Boolean indicating whether there are other bank transaction categories beneath this one in the hierarchy."""
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    parent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parentId'), 'exclude': lambda f: f is None }})
    r"""The unique identifier of the parent bank transaction category."""
    source_modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceModifiedDate'), 'exclude': lambda f: f is None }})
    status: Optional[shared_transactioncategorystatus.TransactionCategoryStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the transaction category."""
    

