"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connection as shared_connection
from ..shared import errormessage as shared_errormessage
from typing import Optional


@dataclasses.dataclass
class GetCompanyConnectionRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})

    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})

    

@dataclasses.dataclass
class GetCompanyConnectionResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    connection: Optional[shared_connection.Connection] = dataclasses.field(default=None)

    r"""OK"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)

    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    