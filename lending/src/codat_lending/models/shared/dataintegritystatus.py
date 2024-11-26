"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dataintegrityamounts import DataIntegrityAmounts, DataIntegrityAmountsTypedDict
from .dataintegrityconnectionid import (
    DataIntegrityConnectionID,
    DataIntegrityConnectionIDTypedDict,
)
from .dataintegritydates import DataIntegrityDates, DataIntegrityDatesTypedDict
from .dataintegritystatusinfo import (
    DataIntegrityStatusInfo,
    DataIntegrityStatusInfoTypedDict,
)
from codat_lending.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DataIntegrityStatusTypedDict(TypedDict):
    amounts: NotRequired[DataIntegrityAmountsTypedDict]
    r"""Only returned for transactions. For accounts, there is nothing returned."""
    connection_ids: NotRequired[DataIntegrityConnectionIDTypedDict]
    dates: NotRequired[DataIntegrityDatesTypedDict]
    r"""Only returned for transactions. For accounts, there is nothing returned."""
    status_info: NotRequired[DataIntegrityStatusInfoTypedDict]
    type: NotRequired[str]
    r"""The data type which the data type in the URL has been matched against. For example, if you've matched accountTransactions and banking-transactions, and you call this endpoint with accountTransactions in the URL, this property would be banking-transactions."""


class DataIntegrityStatus(BaseModel):
    amounts: Optional[DataIntegrityAmounts] = None
    r"""Only returned for transactions. For accounts, there is nothing returned."""

    connection_ids: Annotated[
        Optional[DataIntegrityConnectionID], pydantic.Field(alias="connectionIds")
    ] = None

    dates: Optional[DataIntegrityDates] = None
    r"""Only returned for transactions. For accounts, there is nothing returned."""

    status_info: Annotated[
        Optional[DataIntegrityStatusInfo], pydantic.Field(alias="statusInfo")
    ] = None

    type: Optional[str] = None
    r"""The data type which the data type in the URL has been matched against. For example, if you've matched accountTransactions and banking-transactions, and you call this endpoint with accountTransactions in the URL, this property would be banking-transactions."""