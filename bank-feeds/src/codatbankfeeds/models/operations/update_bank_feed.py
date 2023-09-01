"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bankfeedaccount as shared_bankfeedaccount
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class UpdateBankFeedRequest:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an account"""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    bank_feed_account: Optional[shared_bankfeedaccount.BankFeedAccount] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateBankFeedResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bank_feed_account: Optional[shared_bankfeedaccount.BankFeedAccount] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
