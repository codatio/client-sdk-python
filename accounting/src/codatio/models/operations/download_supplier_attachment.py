from __future__ import annotations
import dataclasses
from ..shared import security as shared_security


@dataclasses.dataclass
class DownloadSupplierAttachmentPathParams:
    attachment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attachmentId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    supplier_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'supplierId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadSupplierAttachmentSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class DownloadSupplierAttachmentRequest:
    path_params: DownloadSupplierAttachmentPathParams = dataclasses.field()
    security: DownloadSupplierAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DownloadSupplierAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    