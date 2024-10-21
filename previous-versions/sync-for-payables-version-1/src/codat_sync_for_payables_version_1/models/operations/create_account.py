"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables_version_1.models.shared import (
    accountprototype as shared_accountprototype,
)
from codat_sync_for_payables_version_1.types import BaseModel
from codat_sync_for_payables_version_1.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateAccountRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    account_prototype: NotRequired[shared_accountprototype.AccountPrototypeTypedDict]
    timeout_in_minutes: NotRequired[int]
    r"""Time limit for the push operation to complete before it is timed out."""


class CreateAccountRequest(BaseModel):
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

    account_prototype: Annotated[
        Optional[shared_accountprototype.AccountPrototype],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    timeout_in_minutes: Annotated[
        Optional[int],
        pydantic.Field(alias="timeoutInMinutes"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Time limit for the push operation to complete before it is timed out."""
