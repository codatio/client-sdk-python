"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_assess.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DataIntegrityMatchTypedDict(TypedDict):
    amount: NotRequired[str]
    r"""The transaction value."""
    connection_id: NotRequired[str]
    r"""ID GUID representing the connection of the accounting or banking platform."""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    date_: NotRequired[str]
    r"""The date of the transaction."""
    description: NotRequired[str]
    r"""The transaction description."""
    id: NotRequired[str]
    r"""ID GUID of the transaction."""
    type: NotRequired[str]
    r"""The data type which the data type in the URL has been matched against. For example, if you've matched accountTransactions and banking-transactions, and you call this endpoint with accountTransactions in the URL, this property would be banking-transactions."""


class DataIntegrityMatch(BaseModel):
    amount: Optional[str] = None
    r"""The transaction value."""

    connection_id: Annotated[Optional[str], pydantic.Field(alias="connectionId")] = None
    r"""ID GUID representing the connection of the accounting or banking platform."""

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    date_: Annotated[Optional[str], pydantic.Field(alias="date")] = None
    r"""The date of the transaction."""

    description: Optional[str] = None
    r"""The transaction description."""

    id: Optional[str] = None
    r"""ID GUID of the transaction."""

    type: Optional[str] = None
    r"""The data type which the data type in the URL has been matched against. For example, if you've matched accountTransactions and banking-transactions, and you call this endpoint with accountTransactions in the URL, this property would be banking-transactions."""
