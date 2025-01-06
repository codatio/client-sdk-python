"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_lending.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TargetAccountOptionTypedDict(TypedDict):
    account_number: NotRequired[Nullable[str]]
    r"""The account number of the account."""
    balance: NotRequired[Nullable[Decimal]]
    r"""The balance of the account."""
    id: NotRequired[str]
    r"""Id of the target account."""
    name: NotRequired[Nullable[str]]
    r"""Name of the target account."""
    sort_code: NotRequired[Nullable[str]]
    r"""The sort code of the account."""


class TargetAccountOption(BaseModel):
    account_number: Annotated[
        OptionalNullable[str], pydantic.Field(alias="accountNumber")
    ] = UNSET
    r"""The account number of the account."""

    balance: Annotated[
        OptionalNullable[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = UNSET
    r"""The balance of the account."""

    id: Optional[str] = None
    r"""Id of the target account."""

    name: OptionalNullable[str] = UNSET
    r"""Name of the target account."""

    sort_code: Annotated[OptionalNullable[str], pydantic.Field(alias="sortCode")] = (
        UNSET
    )
    r"""The sort code of the account."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["accountNumber", "balance", "id", "name", "sortCode"]
        nullable_fields = ["accountNumber", "balance", "name", "sortCode"]
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
