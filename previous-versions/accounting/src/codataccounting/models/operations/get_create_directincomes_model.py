"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import pushoption as shared_pushoption
from typing import Optional



@dataclasses.dataclass
class GetCreateDirectIncomesModelRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetCreateDirectIncomesModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    push_option: Optional[shared_pushoption.PushOption] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

