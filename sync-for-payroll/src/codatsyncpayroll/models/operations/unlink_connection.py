"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connection as shared_connection
from ...models.shared import dataconnectionstatus as shared_dataconnectionstatus
from codatsyncpayroll import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UnlinkConnectionUpdateConnection:
    status: Optional[shared_dataconnectionstatus.DataConnectionStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The current authorization status of the data connection."""
    



@dataclasses.dataclass
class UnlinkConnectionRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    request_body: Optional[UnlinkConnectionUpdateConnection] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UnlinkConnectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None)
    r"""OK"""
    

