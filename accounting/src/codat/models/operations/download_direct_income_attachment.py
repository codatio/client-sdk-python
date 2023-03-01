from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class DownloadDirectIncomeAttachmentPathParams:
    attachment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attachmentId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    direct_income_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'directIncomeId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadDirectIncomeAttachmentSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class DownloadDirectIncomeAttachmentRequest:
    path_params: DownloadDirectIncomeAttachmentPathParams = dataclasses.field()
    security: DownloadDirectIncomeAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DownloadDirectIncomeAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    