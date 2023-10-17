"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class ContactRefContactType(str, Enum):
    r"""The type of contact."""
    SUPPLIER = 'Supplier'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ContactRef:
    contact_type: Optional[ContactRefContactType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contactType'), 'exclude': lambda f: f is None }})
    r"""The type of contact."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""Identifier of supplier or customer."""
    

