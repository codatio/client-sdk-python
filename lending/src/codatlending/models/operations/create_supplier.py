"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import accountingcreatesupplierresponse as shared_accountingcreatesupplierresponse
from ...models.shared import accountingsupplier as shared_accountingsupplier
from typing import Optional


@dataclasses.dataclass
class CreateSupplierRequest:
    UNSET='__SPEAKEASY_UNSET__'
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    accounting_supplier: Optional[shared_accountingsupplier.AccountingSupplier] = dataclasses.field(default=UNSET, metadata={'request': { 'media_type': 'application/json' }})
    allow_sync_on_push_complete: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'allowSyncOnPushComplete', 'style': 'form', 'explode': True }})
    r"""Allow a sync upon push completion."""
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    r"""Time limit for the push operation to complete before it is timed out."""
    



@dataclasses.dataclass
class CreateSupplierResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    accounting_create_supplier_response: Optional[shared_accountingcreatesupplierresponse.AccountingCreateSupplierResponse] = dataclasses.field(default=None)
    r"""Success"""
    

