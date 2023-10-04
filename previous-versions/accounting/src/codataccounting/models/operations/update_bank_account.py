"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bankaccount as shared_bankaccount
from ..shared import errormessage as shared_errormessage
from ..shared import updatebankaccountresponse as shared_updatebankaccountresponse
from typing import Optional



@dataclasses.dataclass
class UpdateBankAccountRequest:
    bank_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'bankAccountId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a bank account."""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    bank_account: Optional[shared_bankaccount.BankAccount] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    force_update: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'forceUpdate', 'style': 'form', 'explode': True }})
    r"""When updating data in the destination platform Codat checks the `sourceModifiedDate` against the `lastupdated` date from the accounting platform, if they're different Codat will return an error suggesting you should initiate another pull of the data. If this is set to `true` then the update will override this check."""
    timeout_in_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'timeoutInMinutes', 'style': 'form', 'explode': True }})
    r"""Time limit for the push operation to complete before it is timed out."""
    




@dataclasses.dataclass
class UpdateBankAccountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    update_bank_account_response: Optional[shared_updatebankaccountresponse.UpdateBankAccountResponse] = dataclasses.field(default=None)
    r"""Success"""
    

