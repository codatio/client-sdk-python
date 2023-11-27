"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import billpayment as shared_billpayment
from typing import Optional


@dataclasses.dataclass
class GetBillPaymentsRequest:
    bill_payment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'billPaymentId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a bill payment."""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    



@dataclasses.dataclass
class GetBillPaymentsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    bill_payment: Optional[shared_billpayment.BillPayment] = dataclasses.field(default=None)
    r"""Success"""
    

