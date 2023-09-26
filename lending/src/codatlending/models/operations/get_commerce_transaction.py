"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import commercetransaction as shared_commercetransaction
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class GetCommerceTransactionRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a transaction."""
    




@dataclasses.dataclass
class GetCommerceTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    commerce_transaction: Optional[shared_commercetransaction.CommerceTransaction] = dataclasses.field(default=None)
    r"""OK"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

