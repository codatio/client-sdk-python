"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import schema as shared_schema
from ..shared import updateexpenserequest as shared_updateexpenserequest
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class UpdateExpenseDatasetRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for your SMB's transaction."""
    update_expense_request: Optional[shared_updateexpenserequest.UpdateExpenseRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class UpdateExpenseDataset202ApplicationJSON:
    r"""Accepted"""
    sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncId'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class UpdateExpenseDatasetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    update_expense_dataset_202_application_json_object: Optional[UpdateExpenseDataset202ApplicationJSON] = dataclasses.field(default=None)
    r"""Accepted"""
    

