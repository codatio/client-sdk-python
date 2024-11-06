"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from enum import Enum
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class StartUploadSessionRequestDataType(str, Enum):
    r"""A key for a Codat data type."""

    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTIONS = "banking-transactions"


class StartUploadSessionRequestTypedDict(TypedDict):
    data_type: NotRequired[StartUploadSessionRequestDataType]
    r"""A key for a Codat data type."""


class StartUploadSessionRequest(BaseModel):
    data_type: Annotated[
        Optional[StartUploadSessionRequestDataType], pydantic.Field(alias="dataType")
    ] = None
    r"""A key for a Codat data type."""
