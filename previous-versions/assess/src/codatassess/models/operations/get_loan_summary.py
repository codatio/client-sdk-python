"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import loansummary as shared_loansummary
from enum import Enum
from typing import Optional

class GetLoanSummaryQueryParamSourceType(str, Enum):
    r"""Data source type."""
    BANKING = 'banking'
    COMMERCE = 'commerce'
    ACCOUNTING = 'accounting'


@dataclasses.dataclass
class GetLoanSummaryRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    source_type: GetLoanSummaryQueryParamSourceType = dataclasses.field(metadata={'query_param': { 'field_name': 'sourceType', 'style': 'form', 'explode': True }})
    r"""Data source type."""
    



@dataclasses.dataclass
class GetLoanSummaryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    loan_summary: Optional[shared_loansummary.LoanSummary] = dataclasses.field(default=None)
    r"""OK"""
    

