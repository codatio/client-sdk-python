"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import financialmetrics as shared_financialmetrics
from typing import Optional



@dataclasses.dataclass
class GetEnhancedFinancialMetricsRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    r"""The number of periods to return. There will be no pagination as a query parameter."""
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    r"""The number of months per period. E.g. 2 = 2 months per period."""
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    r"""The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month."""
    show_metric_inputs: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'showMetricInputs', 'style': 'form', 'explode': True }})
    r"""If set to true, then the system includes the input values within the response."""
    




@dataclasses.dataclass
class GetEnhancedFinancialMetricsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    financial_metrics: Optional[shared_financialmetrics.FinancialMetrics] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

