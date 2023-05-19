"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import dataintegritydatatype as shared_dataintegritydatatype
from ..shared import status as shared_status
from typing import Optional


@dataclasses.dataclass
class GetDataIntegrityStatusRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: shared_dataintegritydatatype.DataIntegrityDataType = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    r"""A key for a Codat data type."""
    

@dataclasses.dataclass
class GetDataIntegrityStatusResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    status: Optional[shared_status.Status] = dataclasses.field(default=None)
    r"""OK"""
    