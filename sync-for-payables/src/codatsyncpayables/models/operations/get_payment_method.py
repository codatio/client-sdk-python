"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import paymentmethod as shared_paymentmethod
from typing import Optional



@dataclasses.dataclass
class GetPaymentMethodRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    payment_method_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'paymentMethodId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a payment method."""
    




@dataclasses.dataclass
class GetPaymentMethodResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    payment_method: Optional[shared_paymentmethod.PaymentMethod] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

