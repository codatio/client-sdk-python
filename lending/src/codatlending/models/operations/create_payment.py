"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import accountingcreatepaymentresponse as shared_accountingcreatepaymentresponse
from ...models.shared import accountingpayment as shared_accountingpayment
from typing import Optional


@dataclasses.dataclass
class CreatePaymentRequest:
    UNSET='__SPEAKEASY_UNSET__'
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    accounting_payment: Optional[shared_accountingpayment.AccountingPayment] = dataclasses.field(default=UNSET, metadata={'request': { 'media_type': 'application/json' }})
    allow_sync_on_push_complete: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'allowSyncOnPushComplete', 'style': 'form', 'explode': True }})
    r"""Allow a sync upon push completion."""
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    r"""Time limit for the push operation to complete before it is timed out."""
    



@dataclasses.dataclass
class CreatePaymentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    accounting_create_payment_response: Optional[shared_accountingcreatepaymentresponse.AccountingCreatePaymentResponse] = dataclasses.field(default=None)
    r"""Success"""
    

