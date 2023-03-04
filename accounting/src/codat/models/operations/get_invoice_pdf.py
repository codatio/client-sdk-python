from __future__ import annotations
import dataclasses
import requests
from typing import Optional


@dataclasses.dataclass
class GetInvoicePdfPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    invoice_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invoiceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetInvoicePdfRequest:
    path_params: GetInvoicePdfPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetInvoicePdfResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    