"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import transactions as shared_transactions
from typing import Optional


@dataclasses.dataclass
class ListSyncTransactionsRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    sync_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a sync."""
    page: Optional[int] = dataclasses.field(default=1, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""
    page_size: Optional[int] = dataclasses.field(default=100, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""
    



@dataclasses.dataclass
class ListSyncTransactionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    transactions: Optional[shared_transactions.Transactions] = dataclasses.field(default=None)
    r"""Success"""
    

