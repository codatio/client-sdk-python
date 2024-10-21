"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables.models.shared import (
    bankaccountprototype as shared_bankaccountprototype,
)
from codat_sync_for_payables.types import BaseModel
from codat_sync_for_payables.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateBankAccountRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    idempotency_key: NotRequired[str]
    r"""A unique identifier to ensure idempotent behaviour for subsequent requests."""
    bank_account_prototype: NotRequired[
        shared_bankaccountprototype.BankAccountPrototypeTypedDict
    ]


class CreateBankAccountRequest(BaseModel):
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

    idempotency_key: Annotated[
        Optional[str],
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""A unique identifier to ensure idempotent behaviour for subsequent requests."""

    bank_account_prototype: Annotated[
        Optional[shared_bankaccountprototype.BankAccountPrototype],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
