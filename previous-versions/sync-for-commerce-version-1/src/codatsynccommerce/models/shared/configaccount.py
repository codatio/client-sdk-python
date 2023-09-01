"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import accountoption as shared_accountoption
from codatsynccommerce import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ConfigAccount:
    r"""G/L account object for configuration."""
    account_options: Optional[list[shared_accountoption.AccountOption]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accountOptions'), 'exclude': lambda f: f is None }})
    r"""Object containing account options."""
    description_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('descriptionText'), 'exclude': lambda f: f is None }})
    r"""Descriprtive text for sales configuration section."""
    label_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('labelText'), 'exclude': lambda f: f is None }})
    r"""Label text for sales configuration section."""
    required: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required'), 'exclude': lambda f: f is None }})
    r"""Required section to be configured for sync."""
    selected_account_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedAccountId'), 'exclude': lambda f: f is None }})
    r"""Selected account id from the list of available accounts."""
    

