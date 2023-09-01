"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import billpayment as shared_billpayment
from ..shared import createbillpaymentresponse as shared_createbillpaymentresponse
from ..shared import schema as shared_schema
from typing import Optional



@dataclasses.dataclass
class CreateBillPaymentRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    bill_payment: Optional[shared_billpayment.BillPayment] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class CreateBillPaymentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_bill_payment_response: Optional[shared_createbillpaymentresponse.CreateBillPaymentResponse] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    schema: Optional[shared_schema.Schema] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    
