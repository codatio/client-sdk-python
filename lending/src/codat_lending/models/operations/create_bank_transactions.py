"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.models.shared import (
    accountingcreatebanktransactions as shared_accountingcreatebanktransactions,
)
from codat_lending.types import BaseModel
from codat_lending.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateBankTransactionsRequestTypedDict(TypedDict):
    account_id: str
    r"""Unique identifier for an account."""
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    accounting_create_bank_transactions: NotRequired[
        shared_accountingcreatebanktransactions.AccountingCreateBankTransactionsTypedDict
    ]
    allow_sync_on_push_complete: NotRequired[bool]
    r"""Allow a sync upon push completion."""
    timeout_in_minutes: NotRequired[int]
    r"""Time limit for the push operation to complete before it is timed out."""


class CreateBankTransactionsRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for an account."""

    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    connection_id: Annotated[
        str,
        pydantic.Field(alias="connectionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a connection."""

    accounting_create_bank_transactions: Annotated[
        Optional[
            shared_accountingcreatebanktransactions.AccountingCreateBankTransactions
        ],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    allow_sync_on_push_complete: Annotated[
        Optional[bool],
        pydantic.Field(alias="allowSyncOnPushComplete"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Allow a sync upon push completion."""

    timeout_in_minutes: Annotated[
        Optional[int],
        pydantic.Field(alias="timeoutInMinutes"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Time limit for the push operation to complete before it is timed out."""
