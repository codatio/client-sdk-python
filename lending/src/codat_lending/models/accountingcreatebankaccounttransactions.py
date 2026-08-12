"""Accounting create-bank-account-transactions response. Synthesized to match Speakeasy's shared surface."""
from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing_extensions import NotRequired, TypedDict
from codat_lending.models.shared.createbankaccounttransaction import CreateBankAccountTransaction, CreateBankAccountTransactionTypedDict


class AccountingCreateBankAccountTransactionsTypedDict(TypedDict):
    account_id: NotRequired[Optional[str]]
    transactions: NotRequired[Optional[List[CreateBankAccountTransactionTypedDict]]]


class AccountingCreateBankAccountTransactions(BaseModel):
    @model_serializer(mode="wrap")
    def _serialize_drop_none(self, handler):
        serialized = handler(self)
        return {k: v for k, v in serialized.items() if v is not None}

    def to_dict(self):
        return self.model_dump(by_alias=True, exclude_none=True)

    @classmethod
    def from_dict(cls, obj):
        return cls.model_validate(obj) if obj is not None else None

    account_id: Optional[str] = Field(default=None, alias="accountId")
    transactions: Optional[List[CreateBankAccountTransaction]] = None

    model_config = ConfigDict(populate_by_name=True, protected_namespaces=())
