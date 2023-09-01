"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import bankingtransaction as shared_bankingtransaction
from typing import Optional



@dataclasses.dataclass
class GetBankingTransactionRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    r"""The unique identifier for a transaction"""
    




@dataclasses.dataclass
class GetBankingTransactionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    banking_transaction: Optional[shared_bankingtransaction.BankingTransaction] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

