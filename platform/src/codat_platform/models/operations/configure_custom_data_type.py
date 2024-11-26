"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.models.shared import (
    customdatatypeconfiguration as shared_customdatatypeconfiguration,
)
from codat_platform.types import BaseModel
from codat_platform.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConfigureCustomDataTypeRequestTypedDict(TypedDict):
    custom_data_identifier: str
    r"""Unique identifier for a custom data type."""
    platform_key: str
    r"""A unique 4-letter key to represent a platform in each integration."""
    custom_data_type_configuration: NotRequired[
        shared_customdatatypeconfiguration.CustomDataTypeConfigurationTypedDict
    ]
    r"""Custom data type configuration for the specified platform."""


class ConfigureCustomDataTypeRequest(BaseModel):
    custom_data_identifier: Annotated[
        str,
        pydantic.Field(alias="customDataIdentifier"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a custom data type."""

    platform_key: Annotated[
        str,
        pydantic.Field(alias="platformKey"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""A unique 4-letter key to represent a platform in each integration."""

    custom_data_type_configuration: Annotated[
        Optional[shared_customdatatypeconfiguration.CustomDataTypeConfiguration],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""Custom data type configuration for the specified platform."""