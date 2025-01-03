"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import BaseModel
import pydantic
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SupplementalDataSourceConfigurationTypedDict(TypedDict):
    r"""The client's defined name for the object."""

    data_source: NotRequired[str]
    r"""The underlying endpoint of the source system which the configuration is targeting."""
    pull_data: NotRequired[Dict[str, str]]
    r"""The additional properties that are required when pulling records."""
    push_data: NotRequired[Dict[str, str]]
    r"""The additional properties that are required to create and/or update records."""


class SupplementalDataSourceConfiguration(BaseModel):
    r"""The client's defined name for the object."""

    data_source: Annotated[Optional[str], pydantic.Field(alias="dataSource")] = None
    r"""The underlying endpoint of the source system which the configuration is targeting."""

    pull_data: Annotated[Optional[Dict[str, str]], pydantic.Field(alias="pullData")] = (
        None
    )
    r"""The additional properties that are required when pulling records."""

    push_data: Annotated[Optional[Dict[str, str]], pydantic.Field(alias="pushData")] = (
        None
    )
    r"""The additional properties that are required to create and/or update records."""


class SupplementalDataConfigurationTypedDict(TypedDict):
    supplemental_data_config: NotRequired[
        Dict[str, SupplementalDataSourceConfigurationTypedDict]
    ]


class SupplementalDataConfiguration(BaseModel):
    supplemental_data_config: Annotated[
        Optional[Dict[str, SupplementalDataSourceConfiguration]],
        pydantic.Field(alias="supplementalDataConfig"),
    ] = None
