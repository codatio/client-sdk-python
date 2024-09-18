"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_commerce.types import BaseModel
from enum import Enum
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class OutputFormat(str, Enum):
    r"""The format commerce transactions are stored in the accounting software."""

    JOURNAL_ENTRY = "JournalEntry"


class ConfigurationMapSettingsTypedDict(TypedDict):
    output_format: NotRequired[OutputFormat]
    r"""The format commerce transactions are stored in the accounting software."""


class ConfigurationMapSettings(BaseModel):
    output_format: Annotated[
        Optional[OutputFormat], pydantic.Field(alias="outputFormat")
    ] = None
    r"""The format commerce transactions are stored in the accounting software."""
