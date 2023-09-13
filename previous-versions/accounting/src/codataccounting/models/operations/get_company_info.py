"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import companydataset as shared_companydataset
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class GetCompanyInfoRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetCompanyInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    company_dataset: Optional[shared_companydataset.CompanyDataset] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

