"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatcommerce import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RecordRef:
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})

    r"""The unique identitifer of the record being referenced"""
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})

    r"""The type of record being referenced."""
    