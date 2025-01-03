"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .datatype import DataType
from codat_platform.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PushOperationTimedOutWebhookDataTypedDict(TypedDict):
    data_type: NotRequired[DataType]
    r"""Available data types"""
    push_operation_guid: NotRequired[str]
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""
    push_operation_key: NotRequired[str]
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""


class PushOperationTimedOutWebhookData(BaseModel):
    data_type: Annotated[Optional[DataType], pydantic.Field(alias="dataType")] = None
    r"""Available data types"""

    push_operation_guid: Annotated[
        Optional[str], pydantic.Field(alias="pushOperationGuid")
    ] = None
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""

    push_operation_key: Annotated[
        Optional[str], pydantic.Field(alias="pushOperationKey")
    ] = None
    r"""A unique identifier generated by Codat to represent this single push operation. This identifier can be used to track the status of the push, and should be persisted."""
