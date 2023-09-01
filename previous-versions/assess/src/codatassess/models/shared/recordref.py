"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class RecordRefIntegrationType(str, Enum):
    r"""The integration type begin referred to."""
    ACCOUNTING = 'Accounting'
    BANKING = 'Banking'
    COMMERCE = 'Commerce'

class RecordRefRecordRefType(str, Enum):
    r"""The datatype being referred to."""
    ACCOUNTS = 'accounts'
    BANKING_ACCOUNTS = 'banking-accounts'
    COMMERCE_TRANSACTIONS = 'commerce-transactions'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RecordRef:
    data_connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataConnectionId'), 'exclude': lambda f: f is None }})
    r"""The dataConnectionId the object being referred to is associated with."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The id of the object being referred to."""
    integration_type: Optional[RecordRefIntegrationType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrationType'), 'exclude': lambda f: f is None }})
    r"""The integration type begin referred to."""
    record_ref_type: Optional[RecordRefRecordRefType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordRefType'), 'exclude': lambda f: f is None }})
    r"""The datatype being referred to."""
    
