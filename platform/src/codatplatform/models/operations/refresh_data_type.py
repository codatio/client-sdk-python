"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import pulloperation as shared_pulloperation
from ...models.shared import schema_datatype as shared_schema_datatype
from typing import Optional


@dataclasses.dataclass
class RefreshDataTypeRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    data_type: shared_schema_datatype.SchemaDataType = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    r"""The key of a Codat data type"""
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'connectionId', 'style': 'form', 'explode': True }})
    r"""Optionally, provide a data connection id to only queue pull operations on that connection."""
    



@dataclasses.dataclass
class RefreshDataTypeResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    pull_operation: Optional[shared_pulloperation.PullOperation] = dataclasses.field(default=None)
    r"""OK"""
    

