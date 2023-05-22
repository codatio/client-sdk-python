"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import dataintegritydatatype as shared_dataintegritydatatype
from ..shared import summaries as shared_summaries
from typing import Optional


@dataclasses.dataclass
class GetDataIntegritySummariesRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: shared_dataintegritydatatype.DataIntegrityDataType = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    r"""A key for a Codat data type."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    r"""Codat query string. [Read more](https://docs.codat.io/using-the-api/querying)."""
    

@dataclasses.dataclass
class GetDataIntegritySummariesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    summaries: Optional[shared_summaries.Summaries] = dataclasses.field(default=None)
    r"""OK"""
    