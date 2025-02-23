"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .syncsetting import SyncSetting, SyncSettingTypedDict
from codat_platform.types import BaseModel
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SyncSettingsTypedDict(TypedDict):
    client_id: NotRequired[str]
    r"""Unique identifier for your client in Codat."""
    overrides_defaults: NotRequired[bool]
    r"""Set to `True` if you want to override the default [sync settings](https://docs.codat.io/knowledge-base/advanced-sync-settings)."""
    settings: NotRequired[List[SyncSettingTypedDict]]


class SyncSettings(BaseModel):
    client_id: Annotated[Optional[str], pydantic.Field(alias="clientId")] = None
    r"""Unique identifier for your client in Codat."""

    overrides_defaults: Annotated[
        Optional[bool], pydantic.Field(alias="overridesDefaults")
    ] = None
    r"""Set to `True` if you want to override the default [sync settings](https://docs.codat.io/knowledge-base/advanced-sync-settings)."""

    settings: Optional[List[SyncSetting]] = None
