"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bankfeedaccountmapping as shared_bankfeedaccountmapping
from ..shared import bankfeedaccountmappingresponse as shared_bankfeedaccountmappingresponse
from ..shared import errormessage as shared_errormessage
from typing import Optional



@dataclasses.dataclass
class CreateBankAccountMappingRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    bank_feed_account_mapping: Optional[shared_bankfeedaccountmapping.BankFeedAccountMapping] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class CreateBankAccountMappingResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bank_feed_account_mapping_response: Optional[shared_bankfeedaccountmappingresponse.BankFeedAccountMappingResponse] = dataclasses.field(default=None)
    r"""Success"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""The request made is not valid."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
