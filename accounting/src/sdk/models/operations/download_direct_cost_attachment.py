from __future__ import annotations
import dataclasses
from ..shared import security as shared_security


@dataclasses.dataclass
class DownloadDirectCostAttachmentPathParams:
    attachment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attachmentId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    direct_cost_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'directCostId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadDirectCostAttachmentSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class DownloadDirectCostAttachmentRequest:
    path_params: DownloadDirectCostAttachmentPathParams = dataclasses.field()
    security: DownloadDirectCostAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DownloadDirectCostAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    