"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import syncrange as shared_syncrange
from ...models.shared import syncsummary as shared_syncsummary
from typing import Optional


@dataclasses.dataclass
class RequestSyncForDateRangeRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    sync_range: Optional[shared_syncrange.SyncRange] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class RequestSyncForDateRangeResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    sync_summary: Optional[shared_syncsummary.SyncSummary] = dataclasses.field(default=None)
    r"""Success"""
    

