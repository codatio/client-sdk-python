"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import loantransactions as shared_loantransactions
from enum import Enum
from typing import Optional

class ListLoanTransactionsQueryParamSourceType(str, Enum):
    r"""Data source type"""
    BANKING = 'banking'
    COMMERCE = 'commerce'
    ACCOUNTING = 'accounting'


@dataclasses.dataclass
class ListLoanTransactionsRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    source_type: ListLoanTransactionsQueryParamSourceType = dataclasses.field(metadata={'query_param': { 'field_name': 'sourceType', 'style': 'form', 'explode': True }})
    r"""Data source type"""
    



@dataclasses.dataclass
class ListLoanTransactionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    loan_transactions: Optional[shared_loantransactions.LoanTransactions] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

