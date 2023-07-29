"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createpurchaseorderresponse as shared_createpurchaseorderresponse
from ..shared import errormessage as shared_errormessage
from ..shared import purchaseorder as shared_purchaseorder
from typing import Optional



@dataclasses.dataclass
class CreatePurchaseOrderRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    purchase_order: Optional[shared_purchaseorder.PurchaseOrder] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class CreatePurchaseOrderResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_purchase_order_response: Optional[shared_createpurchaseorderresponse.CreatePurchaseOrderResponse] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

