"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import periodunit_enum as shared_periodunit_enum
from ..shared import report as shared_report
from typing import Optional


@dataclasses.dataclass
class GetCommerceLifetimeValueMetricsRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    number_of_periods: int = dataclasses.field(metadata={'query_param': { 'field_name': 'numberOfPeriods', 'style': 'form', 'explode': True }})
    r"""The number of periods to return.  There will be no pagination as a query parameter, however Codat will limit the number of periods to request to 12 periods."""  
    period_length: int = dataclasses.field(metadata={'query_param': { 'field_name': 'periodLength', 'style': 'form', 'explode': True }})
    r"""The number of months per period. E.g. 2 = 2 months per period."""  
    period_unit: shared_periodunit_enum.PeriodUnitEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'periodUnit', 'style': 'form', 'explode': True }})
    r"""The period unit of time returned."""  
    report_date: str = dataclasses.field(metadata={'query_param': { 'field_name': 'reportDate', 'style': 'form', 'explode': True }})
    r"""The date in which the report is created up to. Users must specify a specific date, however the response will be provided for the full month."""  
    include_display_names: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeDisplayNames', 'style': 'form', 'explode': True }})
    r"""Shows the dimensionDisplayName and itemDisplayName in measures to make the report data human-readable."""  
    

@dataclasses.dataclass
class GetCommerceLifetimeValueMetricsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    report: Optional[shared_report.Report] = dataclasses.field(default=None)
    r"""OK"""  
    