"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import schema as shared_schema
from ..shared import transfer as shared_transfer
from codataccounting import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class GetTransferRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    transfer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transferId', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetTransfer409ApplicationJSON:
    r"""The data type's dataset has not been requested or is still syncing."""
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetTransferResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_transfer_409_application_json_object: Optional[GetTransfer409ApplicationJSON] = dataclasses.field(default=None)
    r"""The data type's dataset has not been requested or is still syncing."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    transfer: Optional[shared_transfer.Transfer] = dataclasses.field(default=None)
    r"""Success"""
    

