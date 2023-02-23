from __future__ import annotations
import dataclasses
from ..shared import security as shared_security


@dataclasses.dataclass
class PostDirectIncomeAttachmentPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    direct_income_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'directIncomeId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostDirectIncomeAttachmentSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PostDirectIncomeAttachmentRequest:
    path_params: PostDirectIncomeAttachmentPathParams = dataclasses.field()
    security: PostDirectIncomeAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class PostDirectIncomeAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    