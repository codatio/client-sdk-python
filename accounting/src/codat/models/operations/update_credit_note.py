"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import creditnote as shared_creditnote
from ..shared import updatecreditnoteresponse as shared_updatecreditnoteresponse
from typing import Optional


@dataclasses.dataclass
class UpdateCreditNoteRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    credit_note_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'creditNoteId', 'style': 'simple', 'explode': False }})  
    credit_note: Optional[shared_creditnote.CreditNote] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    force_update: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'forceUpdate', 'style': 'form', 'explode': True }})  
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})  
    

@dataclasses.dataclass
class UpdateCreditNoteResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    update_credit_note_response: Optional[shared_updatecreditnoteresponse.UpdateCreditNoteResponse] = dataclasses.field(default=None)
    r"""Success"""  
    