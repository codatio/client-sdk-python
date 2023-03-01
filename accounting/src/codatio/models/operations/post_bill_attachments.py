from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class PostBillAttachmentsPathParams:
    bill_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'billId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PostBillAttachmentsSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class PostBillAttachmentsRequest:
    path_params: PostBillAttachmentsPathParams = dataclasses.field()
    security: PostBillAttachmentsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class PostBillAttachmentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    