"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountcategory as shared_accountcategory
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfirmCategoriesCategoriesAccountRef:
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})

    r"""A unique, persistent identifier for this record"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfirmCategoriesCategories:
    
    account_ref: Optional[ConfirmCategoriesCategoriesAccountRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountRef'), 'exclude': lambda f: f is None }})

    confirmed: Optional[shared_accountcategory.AccountCategory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confirmed'), 'exclude': lambda f: f is None }})

    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConfirmCategories:
    
    categories: Optional[list[ConfirmCategoriesCategories]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categories'), 'exclude': lambda f: f is None }})

    r"""List of confirmed account categories set manually by the user."""
    