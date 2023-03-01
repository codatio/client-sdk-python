from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class GetCompanyCommerceSyncStatusPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompanyCommerceSyncStatusRequest:
    path_params: GetCompanyCommerceSyncStatusPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetCompanyCommerceSyncStatusResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    