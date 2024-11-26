"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_accounting.models.shared import journalprototype as shared_journalprototype
from codat_accounting.types import BaseModel
from codat_accounting.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CreateJournalRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    journal_prototype: NotRequired[shared_journalprototype.JournalPrototypeTypedDict]
    timeout_in_minutes: NotRequired[int]
    r"""Time limit for the push operation to complete before it is timed out."""


class CreateJournalRequest(BaseModel):
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

    journal_prototype: Annotated[
        Optional[shared_journalprototype.JournalPrototype],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None

    timeout_in_minutes: Annotated[
        Optional[int],
        pydantic.Field(alias="timeoutInMinutes"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Time limit for the push operation to complete before it is timed out."""