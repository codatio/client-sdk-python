"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import itemreceipt as shared_itemreceipt
from typing import Optional


@dataclasses.dataclass
class GetItemReceiptRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    item_receipt_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'itemReceiptId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an item receipt."""
    



@dataclasses.dataclass
class GetItemReceiptResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    item_receipt: Optional[shared_itemreceipt.ItemReceipt] = dataclasses.field(default=None)
    r"""Success"""
    

