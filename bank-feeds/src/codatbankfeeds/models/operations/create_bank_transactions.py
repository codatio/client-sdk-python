"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import createbanktransactions as shared_createbanktransactions
from ...models.shared import createbanktransactionsresponse as shared_createbanktransactionsresponse
from typing import Optional


@dataclasses.dataclass
class CreateBankTransactionsRequest:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an account."""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    allow_sync_on_push_complete: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'allowSyncOnPushComplete', 'style': 'form', 'explode': True }})
    r"""Allow a sync upon push completion."""
    create_bank_transactions: Optional[shared_createbanktransactions.CreateBankTransactions] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    r"""Time limit for the push operation to complete before it is timed out."""
    



@dataclasses.dataclass
class CreateBankTransactionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    create_bank_transactions_response: Optional[shared_createbanktransactionsresponse.CreateBankTransactionsResponse] = dataclasses.field(default=None)
    r"""Success"""
    

