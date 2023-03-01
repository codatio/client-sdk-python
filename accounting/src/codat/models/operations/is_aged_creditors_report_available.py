from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class IsAgedCreditorsReportAvailablePathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class IsAgedCreditorsReportAvailableRequest:
    path_params: IsAgedCreditorsReportAvailablePathParams = dataclasses.field()
    

@dataclasses.dataclass
class IsAgedCreditorsReportAvailableResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    is_aged_creditors_report_available_200_application_json_boolean: Optional[bool] = dataclasses.field(default=None)
    