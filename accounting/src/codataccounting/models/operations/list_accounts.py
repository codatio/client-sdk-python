"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accounts as shared_accounts
from typing import Optional


@dataclasses.dataclass
class ListAccountsRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    page: int = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""
    

@dataclasses.dataclass
class ListAccountsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    accounts: Optional[shared_accounts.Accounts] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    