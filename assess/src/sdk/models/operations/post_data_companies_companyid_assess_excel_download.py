from __future__ import annotations
import dataclasses
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcelDownloadPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    
class PostDataCompaniesCompanyIDAssessExcelDownloadReportTypeEnum(str, Enum):
    AUDIT = "audit"


@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcelDownloadQueryParams:
    report_type: PostDataCompaniesCompanyIDAssessExcelDownloadReportTypeEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'reportType', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcelDownloadRequest:
    path_params: PostDataCompaniesCompanyIDAssessExcelDownloadPathParams = dataclasses.field()
    query_params: PostDataCompaniesCompanyIDAssessExcelDownloadQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcelDownloadResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    