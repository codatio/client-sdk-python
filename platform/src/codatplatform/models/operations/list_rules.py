"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import webhooks as shared_webhooks
from typing import Callable, Optional



@dataclasses.dataclass
class ListRulesRequest:
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results)."""
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""Page number. [Read more](https://docs.codat.io/using-the-api/paging)."""
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging)."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""
    




@dataclasses.dataclass
class ListRulesResponse:
    next: Callable[[], Optional[ListRulesResponse]] = dataclasses.field()
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your `query` parameter was not correctly formed"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    webhooks: Optional[shared_webhooks.Webhooks] = dataclasses.field(default=None)
    r"""OK"""
    

