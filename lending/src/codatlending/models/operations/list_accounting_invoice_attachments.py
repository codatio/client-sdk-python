"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import attachments as shared_attachments
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class ListAccountingInvoiceAttachmentsRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    invoice_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invoiceId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an invoice"""
    




@dataclasses.dataclass
class ListAccountingInvoiceAttachmentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    attachments: Optional[shared_attachments.Attachments] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
