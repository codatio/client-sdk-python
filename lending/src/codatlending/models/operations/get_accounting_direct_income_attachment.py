"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accountingattachment as shared_accountingattachment
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class GetAccountingDirectIncomeAttachmentRequest:
    attachment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attachmentId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an attachment"""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    direct_income_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'directIncomeId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a direct income"""
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class GetAccountingDirectIncomeAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    accounting_attachment: Optional[shared_accountingattachment.AccountingAttachment] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

