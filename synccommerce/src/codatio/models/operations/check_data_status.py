from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class CheckDataStatusPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'datasetId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CheckDataStatusRequest:
    path_params: CheckDataStatusPathParams = dataclasses.field()
    

@dataclasses.dataclass
class CheckDataStatusResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    