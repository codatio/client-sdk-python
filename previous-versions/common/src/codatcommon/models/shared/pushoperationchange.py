"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import pushchangetype as shared_pushchangetype
from ..shared import pushoperationref as shared_pushoperationref
from codatcommon import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PushOperationChange:
    attachment_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attachmentId') }})
    r"""Unique identifier for the attachment created otherwise null."""
    record_ref: Optional[shared_pushoperationref.PushOperationRef] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRef'), 'exclude': lambda f: f is None }})
    type: Optional[shared_pushchangetype.PushChangeType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Type of change being applied to record in third party platform."""
    

