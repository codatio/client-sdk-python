"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import attachment as shared_attachment
from typing import Optional


@dataclasses.dataclass
class UploadAttachmentRequestBody:
    
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})  
    request_body: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'requestBody' }})  
    

@dataclasses.dataclass
class UploadAttachmentRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    sync_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a sync."""  
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for your SMB's transaction."""  
    request_body: Optional[UploadAttachmentRequestBody] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }, 'request': { 'media_type': 'multipart/form-data' }})  
    

@dataclasses.dataclass
class UploadAttachmentResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    attachment: Optional[shared_attachment.Attachment] = dataclasses.field(default=None)
    r"""OK"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    