from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class DonwloadInvoiceAttachmentPathParams:
    attachment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attachmentId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    invoice_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invoiceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DonwloadInvoiceAttachmentSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class DonwloadInvoiceAttachmentRequest:
    path_params: DonwloadInvoiceAttachmentPathParams = dataclasses.field()
    security: DonwloadInvoiceAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DonwloadInvoiceAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    