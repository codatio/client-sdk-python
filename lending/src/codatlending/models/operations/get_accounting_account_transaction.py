"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accountingaccounttransaction as shared_accountingaccounttransaction
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class GetAccountingAccountTransactionRequest:
    account_transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountTransactionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an account transaction."""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    




@dataclasses.dataclass
class GetAccountingAccountTransactionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    accounting_account_transaction: Optional[shared_accountingaccounttransaction.AccountingAccountTransaction] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

