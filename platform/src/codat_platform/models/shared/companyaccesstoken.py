"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class CompanyAccessTokenTypedDict(TypedDict):
    r"""Details of the access token provisioned for a company."""

    access_token: str
    r"""The access token for the company."""
    expires_in: int
    r"""The number of seconds until the access token expires."""
    token_type: str
    r"""The type of token."""


class CompanyAccessToken(BaseModel):
    r"""Details of the access token provisioned for a company."""

    access_token: Annotated[str, pydantic.Field(alias="accessToken")]
    r"""The access token for the company."""

    expires_in: Annotated[int, pydantic.Field(alias="expiresIn")]
    r"""The number of seconds until the access token expires."""

    token_type: Annotated[str, pydantic.Field(alias="tokenType")]
    r"""The type of token."""
