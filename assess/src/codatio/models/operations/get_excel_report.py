from __future__ import annotations
import dataclasses
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class GetExcelReportPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    
class GetExcelReportReportTypeEnum(str, Enum):
    AUDIT = "audit"


@dataclasses.dataclass
class GetExcelReportQueryParams:
    report_type: GetExcelReportReportTypeEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'reportType', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetExcelReportRequest:
    path_params: GetExcelReportPathParams = dataclasses.field()
    query_params: GetExcelReportQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetExcelReportResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    