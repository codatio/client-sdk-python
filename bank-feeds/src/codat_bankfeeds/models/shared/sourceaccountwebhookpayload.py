"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .companyreference import CompanyReference, CompanyReferenceTypedDict
from .sourceaccount import SourceAccount, SourceAccountTypedDict
from .sourceaccountv2 import SourceAccountV2, SourceAccountV2TypedDict
from codat_bankfeeds.types import BaseModel
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


SourceAccountWebhookPayloadSourceAccountTypedDict = TypeAliasType(
    "SourceAccountWebhookPayloadSourceAccountTypedDict",
    Union[SourceAccountTypedDict, SourceAccountV2TypedDict],
)


SourceAccountWebhookPayloadSourceAccount = TypeAliasType(
    "SourceAccountWebhookPayloadSourceAccount", Union[SourceAccount, SourceAccountV2]
)


class SourceAccountWebhookPayloadTypedDict(TypedDict):
    company_id: NotRequired[str]
    r"""Unique identifier for your SMB in Codat."""
    connection_id: NotRequired[str]
    r"""Unique identifier for a company's data connection."""
    reference_company: NotRequired[CompanyReferenceTypedDict]
    source_account: NotRequired[SourceAccountWebhookPayloadSourceAccountTypedDict]


class SourceAccountWebhookPayload(BaseModel):
    company_id: Annotated[Optional[str], pydantic.Field(alias="companyId")] = None
    r"""Unique identifier for your SMB in Codat."""

    connection_id: Annotated[Optional[str], pydantic.Field(alias="connectionId")] = None
    r"""Unique identifier for a company's data connection."""

    reference_company: Annotated[
        Optional[CompanyReference], pydantic.Field(alias="referenceCompany")
    ] = None

    source_account: Annotated[
        Optional[SourceAccountWebhookPayloadSourceAccount],
        pydantic.Field(alias="sourceAccount"),
    ] = None
