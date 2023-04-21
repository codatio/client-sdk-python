"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import salesorder as shared_salesorder
from typing import Optional


@dataclasses.dataclass
class GetSalesOrderRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    sales_order_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'salesOrderId', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class GetSalesOrderResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    sales_order: Optional[shared_salesorder.SalesOrder] = dataclasses.field(default=None)
    r"""Success"""  
    