"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import updateexpenserequest as shared_updateexpenserequest
from ...models.shared import updateexpenseresponse as shared_updateexpenseresponse
from typing import Optional


@dataclasses.dataclass
class UpdateExpenseTransactionRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for your SMB's transaction."""
    update_expense_request: Optional[shared_updateexpenserequest.UpdateExpenseRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateExpenseTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_expense_response: Optional[shared_updateexpenseresponse.UpdateExpenseResponse] = dataclasses.field(default=None)
    r"""Accepted"""
    

