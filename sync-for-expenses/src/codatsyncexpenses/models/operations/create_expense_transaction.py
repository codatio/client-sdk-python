"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createexpenserequest as shared_createexpenserequest
from ..shared import createexpenseresponse as shared_createexpenseresponse
from ..shared import errormessage as shared_errormessage
from typing import Optional


@dataclasses.dataclass
class CreateExpenseTransactionRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    create_expense_request: Optional[shared_createexpenserequest.CreateExpenseRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class CreateExpenseTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_expense_response: Optional[shared_createexpenseresponse.CreateExpenseResponse] = dataclasses.field(default=None)
    r"""OK"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

