"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import excelreporttypes as shared_excelreporttypes
from ..shared import excelstatus as shared_excelstatus
from typing import Optional



@dataclasses.dataclass
class GetExcelReportGenerationStatusRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    report_type: shared_excelreporttypes.ExcelReportTypes = dataclasses.field(metadata={'query_param': { 'field_name': 'reportType', 'style': 'form', 'explode': True }})
    r"""The type of report you want to generate and download."""
    




@dataclasses.dataclass
class GetExcelReportGenerationStatusResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    excel_status: Optional[shared_excelstatus.ExcelStatus] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

