"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createexpenserequest as shared_createexpenserequest
from ..shared import createexpenseresponse as shared_createexpenseresponse
from typing import Optional


@dataclasses.dataclass
class CreateExpenseDatasetRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    create_expense_request: Optional[shared_createexpenserequest.CreateExpenseRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class CreateExpenseDatasetResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    create_expense_response: Optional[shared_createexpenseresponse.CreateExpenseResponse] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    