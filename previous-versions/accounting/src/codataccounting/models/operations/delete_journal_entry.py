"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import pushoperationsummary as shared_pushoperationsummary
from typing import Optional


@dataclasses.dataclass
class DeleteJournalEntryRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    journal_entry_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'journalEntryId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a journal entry."""
    



@dataclasses.dataclass
class DeleteJournalEntryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    push_operation_summary: Optional[shared_pushoperationsummary.PushOperationSummary] = dataclasses.field(default=None)
    r"""OK"""
    

