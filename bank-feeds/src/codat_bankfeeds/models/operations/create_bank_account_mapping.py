"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_bankfeeds.models.shared import (
    bankfeedaccountmapping as shared_bankfeedaccountmapping,
)
from codat_bankfeeds.types import BaseModel
from codat_bankfeeds.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateBankAccountMappingRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    bank_feed_account_mapping: NotRequired[
        shared_bankfeedaccountmapping.BankFeedAccountMappingTypedDict
    ]


class CreateBankAccountMappingRequest(BaseModel):
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

    bank_feed_account_mapping: Annotated[
        Optional[shared_bankfeedaccountmapping.BankFeedAccountMapping],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
