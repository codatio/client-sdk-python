"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import connectionmanagementaccesstoken as shared_connectionmanagementaccesstoken
from typing import Optional


@dataclasses.dataclass
class GetConnectionManagementAccessTokenRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    



@dataclasses.dataclass
class GetConnectionManagementAccessTokenResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    connection_management_access_token: Optional[shared_connectionmanagementaccesstoken.ConnectionManagementAccessToken] = dataclasses.field(default=None)
    r"""Success"""
    

