from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class DownloadBillAttachmentPathParams:
    attachment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attachmentId', 'style': 'simple', 'explode': False }})
    bill_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'billId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadBillAttachmentSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class DownloadBillAttachmentRequest:
    path_params: DownloadBillAttachmentPathParams = dataclasses.field()
    security: DownloadBillAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DownloadBillAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    