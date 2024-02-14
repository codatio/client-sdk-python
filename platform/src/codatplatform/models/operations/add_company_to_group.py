"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import company as shared_company
from ...models.shared import companygroupassignment as shared_companygroupassignment
from typing import Optional


@dataclasses.dataclass
class AddCompanyToGroupRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    company_group_assignment: Optional[shared_companygroupassignment.CompanyGroupAssignment] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class AddCompanyToGroupResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    company: Optional[shared_company.Company] = dataclasses.field(default=None)
    r"""Success"""
    

