"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .brandingimage import BrandingImage, BrandingImageTypedDict
from codat_sync_for_commerce.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class BrandingButtonTypedDict(TypedDict):
    r"""Button branding references."""

    default: NotRequired[BrandingImageTypedDict]
    hover: NotRequired[BrandingImageTypedDict]


class BrandingButton(BaseModel):
    r"""Button branding references."""

    default: Optional[BrandingImage] = None

    hover: Optional[BrandingImage] = None
