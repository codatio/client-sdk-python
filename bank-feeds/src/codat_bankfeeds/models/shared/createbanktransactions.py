"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .banktransactions import BankTransactions, BankTransactionsTypedDict
from codat_bankfeeds.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class CreateBankTransactionsTypedDict(TypedDict):
    account_id: str
    r"""Unique identifier for a bank account."""
    transactions: List[BankTransactionsTypedDict]


class CreateBankTransactions(BaseModel):
    account_id: Annotated[str, pydantic.Field(alias="accountId")]
    r"""Unique identifier for a bank account."""

    transactions: List[BankTransactions]
