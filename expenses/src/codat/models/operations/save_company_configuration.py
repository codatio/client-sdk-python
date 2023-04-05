"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import codaterrormessage as shared_codaterrormessage
from ..shared import companyconfiguration as shared_companyconfiguration
from typing import Optional


@dataclasses.dataclass
class SaveCompanyConfigurationRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    company_configuration: Optional[shared_companyconfiguration.CompanyConfiguration] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})  
    

@dataclasses.dataclass
class SaveCompanyConfigurationResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    codat_error_message: Optional[shared_codaterrormessage.CodatErrorMessage] = dataclasses.field(default=None)
    r"""Bad Request"""  
    company_configuration: Optional[shared_companyconfiguration.CompanyConfiguration] = dataclasses.field(default=None)
    r"""Success"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    