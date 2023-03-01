from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class DownloadCustomerAttachmentPathParams:
    attachment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attachmentId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    customer_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'customerId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadCustomerAttachmentSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class DownloadCustomerAttachmentRequest:
    path_params: DownloadCustomerAttachmentPathParams = dataclasses.field()
    security: DownloadCustomerAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DownloadCustomerAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    