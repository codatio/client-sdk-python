"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class BankFeedBankAccountMappingTypedDict(TypedDict):
    source_account_id: str
    r"""Unique ID for the source account"""
    target_account_id: NotRequired[Nullable[str]]
    r"""Unique ID for the target account"""


class BankFeedBankAccountMapping(BaseModel):
    source_account_id: Annotated[str, pydantic.Field(alias="sourceAccountId")]
    r"""Unique ID for the source account"""

    target_account_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="targetAccountId")
    ] = UNSET
    r"""Unique ID for the target account"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["targetAccountId"]
        nullable_fields = ["targetAccountId"]
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