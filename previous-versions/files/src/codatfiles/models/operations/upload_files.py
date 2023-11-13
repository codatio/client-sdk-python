"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class UploadFilesRequestBody:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file_name: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'fileName' }})
    



@dataclasses.dataclass
class UploadFilesRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    request_body: Optional[UploadFilesRequestBody] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }, 'request': { 'media_type': 'multipart/form-data' }})
    



@dataclasses.dataclass
class UploadFilesResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

