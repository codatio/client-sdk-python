from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class GetInvoicePdfPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    invoice_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invoiceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetInvoicePdfSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetInvoicePdfRequest:
    path_params: GetInvoicePdfPathParams = dataclasses.field()
    security: GetInvoicePdfSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetInvoicePdfResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    