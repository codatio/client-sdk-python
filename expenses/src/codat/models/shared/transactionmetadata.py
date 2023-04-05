"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import integrationtype_enum as shared_integrationtype_enum
from ..shared import transactionstatus_enum as shared_transactionstatus_enum
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TransactionMetadata:
    
    integration_type: Optional[shared_integrationtype_enum.IntegrationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrationType'), 'exclude': lambda f: f is None }})
    r"""Type of transaction that has been processed e.g. Expense or Bank Feed."""  
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Metadata such as validation errors or the resulting record created in the accounting software."""  
    status: Optional[shared_transactionstatus_enum.TransactionStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Status of the transaction."""  
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactionId'), 'exclude': lambda f: f is None }})
    r"""Your unique idenfier of the transaction."""  
    