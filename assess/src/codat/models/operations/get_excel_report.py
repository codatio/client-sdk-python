from __future__ import annotations
import dataclasses
import requests as requests_http
from enum import Enum
from typing import Optional

class GetExcelReportReportTypeEnum(str, Enum):
    AUDIT = "audit"


@dataclasses.dataclass
class GetExcelReportRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    report_type: GetExcelReportReportTypeEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'reportType', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetExcelReportResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    