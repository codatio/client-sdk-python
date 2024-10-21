"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables_version_1.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from codat_sync_for_payables_version_1.utils import serialize_decimal, validate_decimal
from decimal import Decimal
import pydantic
from pydantic import model_serializer
from pydantic.functional_serializers import PlainSerializer
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated, NotRequired, TypedDict


class TaxRateComponentTypedDict(TypedDict):
    r"""A tax rate can be made up of multiple sub taxes, often called components of the tax."""

    is_compound: bool
    r"""A flag to indicate with the tax is calculated using the principle of compounding."""
    name: NotRequired[Nullable[str]]
    r"""Name of the tax rate component."""
    rate: NotRequired[Nullable[Decimal]]
    r"""The rate of the tax rate component, usually a percentage."""


class TaxRateComponent(BaseModel):
    r"""A tax rate can be made up of multiple sub taxes, often called components of the tax."""

    is_compound: Annotated[bool, pydantic.Field(alias="isCompound")]
    r"""A flag to indicate with the tax is calculated using the principle of compounding."""

    name: OptionalNullable[str] = UNSET
    r"""Name of the tax rate component."""

    rate: Annotated[
        OptionalNullable[Decimal],
        BeforeValidator(validate_decimal),
        PlainSerializer(serialize_decimal(False)),
    ] = UNSET
    r"""The rate of the tax rate component, usually a percentage."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "rate"]
        nullable_fields = ["name", "rate"]
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
