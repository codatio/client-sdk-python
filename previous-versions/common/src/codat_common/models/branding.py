"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .brandingbutton import BrandingButton, BrandingButtonTypedDict
from .brandinglogo import BrandingLogo, BrandingLogoTypedDict
from codat_common.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class BrandingTypedDict(TypedDict):
    button: NotRequired[BrandingButtonTypedDict]
    r"""Button branding references."""
    logo: NotRequired[BrandingLogoTypedDict]
    r"""Logo branding references."""
    source_id: NotRequired[str]
    r"""A source-specific ID used to distinguish between different sources originating from the same data connection. In general, a data connection is a single data source. However, for TrueLayer, `sourceId` is associated with a specific bank and has a many-to-one relationship with the `integrationId`."""


class Branding(BaseModel):
    button: Optional[BrandingButton] = None
    r"""Button branding references."""

    logo: Optional[BrandingLogo] = None
    r"""Logo branding references."""

    source_id: Annotated[Optional[str], pydantic.Field(alias="sourceId")] = None
    r"""A source-specific ID used to distinguish between different sources originating from the same data connection. In general, a data connection is a single data source. However, for TrueLayer, `sourceId` is associated with a specific bank and has a many-to-one relationship with the `integrationId`."""
