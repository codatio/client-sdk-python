"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import attachmentupload as shared_attachmentupload
from typing import Optional


@dataclasses.dataclass
class UploadDirectCostAttachmentRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    direct_cost_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'directCostId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a direct cost."""
    attachment_upload: Optional[shared_attachmentupload.AttachmentUpload] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    



@dataclasses.dataclass
class UploadDirectCostAttachmentResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    

