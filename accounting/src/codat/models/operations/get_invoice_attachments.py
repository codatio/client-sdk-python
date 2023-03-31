"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import attachmentsdataset as shared_attachmentsdataset
from typing import Optional


@dataclasses.dataclass
class GetInvoiceAttachmentsRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})  
    invoice_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invoiceId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an invoice"""  
    

@dataclasses.dataclass
class GetInvoiceAttachmentsResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    attachments_dataset: Optional[shared_attachmentsdataset.AttachmentsDataset] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    