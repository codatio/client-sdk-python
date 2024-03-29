"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import creditnote as shared_creditnote
from typing import Optional


@dataclasses.dataclass
class GetCreditNoteRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    credit_note_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'creditNoteId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a credit note."""
    



@dataclasses.dataclass
class GetCreditNoteResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    credit_note: Optional[shared_creditnote.CreditNote] = dataclasses.field(default=None)
    r"""Success"""
    

