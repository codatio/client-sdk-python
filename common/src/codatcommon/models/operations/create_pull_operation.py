"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import datatype_enum as shared_datatype_enum
from ..shared import errormessage as shared_errormessage
from ..shared import pulloperation as shared_pulloperation
from typing import Optional


@dataclasses.dataclass
class CreatePullOperationRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: shared_datatype_enum.DataTypeEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    r"""The key of a Codat data type"""
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'connectionId', 'style': 'form', 'explode': True }})
    r"""Optionally, provide a data connection id to only queue pull operations on that connection."""
    

@dataclasses.dataclass
class CreatePullOperationResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    pull_operation: Optional[shared_pulloperation.PullOperation] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    