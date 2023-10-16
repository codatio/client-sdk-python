"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bankingtransactioncategory as shared_bankingtransactioncategory
from typing import Optional



@dataclasses.dataclass
class GetBankingTransactionCategoryRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    transaction_category_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionCategoryId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for a banking transaction category"""
    




@dataclasses.dataclass
class GetBankingTransactionCategoryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    banking_transaction_category: Optional[shared_bankingtransactioncategory.BankingTransactionCategory] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

