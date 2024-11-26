"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .syncasbankfeeds import SyncAsBankFeeds, SyncAsBankFeedsTypedDict
from .syncasexpenses import SyncAsExpenses, SyncAsExpensesTypedDict
from codat_bankfeeds.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SyncConfigurationTypedDict(TypedDict):
    sync_as_bank_feeds: NotRequired[SyncAsBankFeedsTypedDict]
    sync_as_expenses: NotRequired[SyncAsExpensesTypedDict]


class SyncConfiguration(BaseModel):
    sync_as_bank_feeds: Annotated[
        Optional[SyncAsBankFeeds], pydantic.Field(alias="syncAsBankFeeds")
    ] = None

    sync_as_expenses: Annotated[
        Optional[SyncAsExpenses], pydantic.Field(alias="syncAsExpenses")
    ] = None