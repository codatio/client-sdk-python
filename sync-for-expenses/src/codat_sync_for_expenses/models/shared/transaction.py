"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_expenses.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TransactionDefinitionsStatus(str, Enum):
    r"""Status of transaction."""

    UNKNOWN = "Unknown"
    PUSH_ERROR = "PushError"
    COMPLETED = "Completed"
    FAILED = "Failed"
    PENDING = "Pending"


class TransactionTypedDict(TypedDict):
    error_message: NotRequired[Nullable[str]]
    r"""Error message for failed transaction."""
    id: NotRequired[str]
    r"""Unique identifier of the transaction."""
    status: NotRequired[TransactionDefinitionsStatus]
    r"""Status of transaction."""


class Transaction(BaseModel):
    error_message: Annotated[
        OptionalNullable[str], pydantic.Field(alias="errorMessage")
    ] = UNSET
    r"""Error message for failed transaction."""

    id: Optional[str] = None
    r"""Unique identifier of the transaction."""

    status: Optional[TransactionDefinitionsStatus] = None
    r"""Status of transaction."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["errorMessage", "id", "status"]
        nullable_fields = ["errorMessage"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
