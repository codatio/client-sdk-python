from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class PostDirectCostAttachmentPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    direct_cost_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'directCostId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostDirectCostAttachmentSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class PostDirectCostAttachmentRequest:
    path_params: PostDirectCostAttachmentPathParams = dataclasses.field()
    security: PostDirectCostAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class PostDirectCostAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    