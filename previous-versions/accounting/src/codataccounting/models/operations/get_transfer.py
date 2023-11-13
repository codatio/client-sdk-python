"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import transfer as shared_transfer
from typing import Optional


@dataclasses.dataclass
class GetTransferRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    transfer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transferId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a transfer."""
    



@dataclasses.dataclass
class GetTransferResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    transfer: Optional[shared_transfer.Transfer] = dataclasses.field(default=None)
    r"""Success"""
    

