from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class CreateDataConnectionPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateDataConnectionRequest:
    path_params: CreateDataConnectionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class CreateDataConnectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    