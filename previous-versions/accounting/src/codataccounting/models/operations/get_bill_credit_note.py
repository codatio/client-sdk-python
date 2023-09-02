"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import billcreditnote as shared_billcreditnote
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class GetBillCreditNoteRequest:
    bill_credit_note_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'billCreditNoteId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetBillCreditNoteResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bill_credit_note: Optional[shared_billcreditnote.BillCreditNote] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

