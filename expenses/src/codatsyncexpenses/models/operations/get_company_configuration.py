"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import companyconfiguration as shared_companyconfiguration
from typing import Optional


@dataclasses.dataclass
class GetCompanyConfigurationRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetCompanyConfigurationResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    company_configuration: Optional[shared_companyconfiguration.CompanyConfiguration] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    