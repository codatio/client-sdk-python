"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accounts import Accounts, AccountsTypedDict
from codat_lending.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DataSourceTypedDict(TypedDict):
    accounts: NotRequired[List[AccountsTypedDict]]
    r"""An array containing bank account data for each connected banking data source that have the following data types enabled: `banking-accounts`, `banking-transactions`."""


class DataSource(BaseModel):
    accounts: Optional[List[Accounts]] = None
    r"""An array containing bank account data for each connected banking data source that have the following data types enabled: `banking-accounts`, `banking-transactions`."""
