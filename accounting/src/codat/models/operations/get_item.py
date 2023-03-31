"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import item as shared_item
from typing import Optional


@dataclasses.dataclass
class GetItemRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    item_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'itemId', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class GetItemResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    item: Optional[shared_item.Item] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    