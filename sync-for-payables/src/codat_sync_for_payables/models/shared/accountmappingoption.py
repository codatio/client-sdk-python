"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountstatus import AccountStatus
from codat_sync_for_payables.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountMappingOptionTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Identifier for the account, unique for the company."""
    nominal_code: NotRequired[Nullable[str]]
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""
    name: NotRequired[Nullable[str]]
    r"""Name of the account."""
    type: NotRequired[Nullable[str]]
    r"""Type of account."""
    currency: NotRequired[str]
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """
    status: NotRequired[AccountStatus]
    r"""The current status of the account."""
    source_modified_date: NotRequired[str]


class AccountMappingOption(BaseModel):
    id: Optional[str] = None
    r"""Identifier for the account, unique for the company."""

    nominal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="nominalCode")
    ] = UNSET
    r"""Reference given to each nominal account for a business. It ensures money is allocated to the correct account. This code isn't a unique identifier in the Codat system."""

    name: OptionalNullable[str] = UNSET
    r"""Name of the account."""

    type: OptionalNullable[str] = UNSET
    r"""Type of account."""

    currency: Optional[str] = None
    r"""The currency data type in Codat is the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency code, e.g. _GBP_.

    ## Unknown currencies

    In line with the ISO 4217 specification, the code _XXX_ is used when the data source does not return a currency for a transaction.

    There are only a very small number of edge cases where this currency code is returned by the Codat system.
    """

    status: Optional[AccountStatus] = None
    r"""The current status of the account."""

    source_modified_date: Annotated[
        Optional[str], pydantic.Field(alias="sourceModifiedDate")
    ] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "nominalCode",
            "name",
            "type",
            "currency",
            "status",
            "sourceModifiedDate",
        ]
        nullable_fields = ["nominalCode", "name", "type"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m