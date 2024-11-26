"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import BaseModel
from codat_platform.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateConnectionRequestBodyTypedDict(TypedDict):
    platform_key: NotRequired[str]
    r"""A unique 4-letter key to represent a platform in each integration. View [accounting](https://docs.codat.io/integrations/accounting/overview#platform-keys), [banking](https://docs.codat.io/integrations/banking/overview#platform-keys), and [commerce](https://docs.codat.io/integrations/commerce/overview#platform-keys) platform keys."""


class CreateConnectionRequestBody(BaseModel):
    platform_key: Annotated[Optional[str], pydantic.Field(alias="platformKey")] = None
    r"""A unique 4-letter key to represent a platform in each integration. View [accounting](https://docs.codat.io/integrations/accounting/overview#platform-keys), [banking](https://docs.codat.io/integrations/banking/overview#platform-keys), and [commerce](https://docs.codat.io/integrations/commerce/overview#platform-keys) platform keys."""


class CreateConnectionRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    request_body: NotRequired[CreateConnectionRequestBodyTypedDict]


class CreateConnectionRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    request_body: Annotated[
        Optional[CreateConnectionRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
