import dataclasses
from ..shared import security as shared_security


@dataclasses.dataclass
class PushInvoiceAttachmentPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    invoice_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invoiceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PushInvoiceAttachmentSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PushInvoiceAttachmentRequest:
    path_params: PushInvoiceAttachmentPathParams = dataclasses.field()
    security: PushInvoiceAttachmentSecurity = dataclasses.field()
    

@dataclasses.dataclass
class PushInvoiceAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    