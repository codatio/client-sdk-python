"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import transactioncategory as shared_transactioncategory
from typing import Optional



@dataclasses.dataclass
class GetTransactionCategoryRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    transaction_category_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionCategoryId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for a banking transaction category"""
    




@dataclasses.dataclass
class GetTransactionCategoryResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    transaction_category: Optional[shared_transactioncategory.TransactionCategory] = dataclasses.field(default=None)
    r"""Success"""
    

