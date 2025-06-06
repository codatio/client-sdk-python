"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ProfileTypedDict(TypedDict):
    r"""Describes your Codat client instance"""

    name: str
    r"""The name given to the instance."""
    redirect_url: str
    r"""The redirect URL pasted on to the SMB once Codat's [Hosted Link](https://docs.codat.io/auth-flow/authorize-hosted-link) has been completed by the SMB."""
    api_key: NotRequired[str]
    r"""The API key for this Codat instance."""
    confirm_company_name: NotRequired[bool]
    r"""`True` if the company name has been confirmed."""
    icon_url: NotRequired[str]
    r"""Static url to your organization's icon."""
    logo_url: NotRequired[str]
    r"""Static url to your organization's logo."""
    white_list_urls: NotRequired[List[str]]
    r"""A list of urls that are allowed to communicate with Codat. If empty any url is allowed to communicate with Codat."""


class Profile(BaseModel):
    r"""Describes your Codat client instance"""

    name: str
    r"""The name given to the instance."""

    redirect_url: Annotated[str, pydantic.Field(alias="redirectUrl")]
    r"""The redirect URL pasted on to the SMB once Codat's [Hosted Link](https://docs.codat.io/auth-flow/authorize-hosted-link) has been completed by the SMB."""

    api_key: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="apiKey",
        ),
    ] = None
    r"""The API key for this Codat instance."""

    confirm_company_name: Annotated[
        Optional[bool],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="confirmCompanyName",
        ),
    ] = None
    r"""`True` if the company name has been confirmed."""

    icon_url: Annotated[Optional[str], pydantic.Field(alias="iconUrl")] = None
    r"""Static url to your organization's icon."""

    logo_url: Annotated[Optional[str], pydantic.Field(alias="logoUrl")] = None
    r"""Static url to your organization's logo."""

    white_list_urls: Annotated[
        Optional[List[str]], pydantic.Field(alias="whiteListUrls")
    ] = None
    r"""A list of urls that are allowed to communicate with Codat. If empty any url is allowed to communicate with Codat."""
