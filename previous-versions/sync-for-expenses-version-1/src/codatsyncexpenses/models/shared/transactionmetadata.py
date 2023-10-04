"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import integrationtype as shared_integrationtype
from ..shared import transactionstatus as shared_transactionstatus
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TransactionMetadata:
    integration_type: Optional[shared_integrationtype.IntegrationType] = dataclasses.field(default=shared_integrationtype.IntegrationType.EXPENSES, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('integrationType') }})
    r"""Type of transaction that has been processed e.g. Expense or Bank Feed."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""Metadata such as validation errors or the resulting record created in the accounting software."""
    status: Optional[shared_transactionstatus.TransactionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Status of the transaction."""
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactionId') }})
    r"""Your unique idenfier of the transaction."""
    

