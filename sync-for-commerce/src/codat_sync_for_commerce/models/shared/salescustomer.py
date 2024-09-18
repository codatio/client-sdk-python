"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .configurationoption import ConfigurationOption, ConfigurationOptionTypedDict
from codat_sync_for_commerce.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, TypedDict
from typing_extensions import Annotated, NotRequired


class SalesCustomerTypedDict(TypedDict):
    customer_options: NotRequired[Nullable[List[ConfigurationOptionTypedDict]]]
    r"""List of customer options from the list of customer records on the accounting software."""
    selected_customer_id: NotRequired[Nullable[str]]
    r"""Selected customer id from the list of customer records on the accounting software."""


class SalesCustomer(BaseModel):
    customer_options: Annotated[
        OptionalNullable[List[ConfigurationOption]],
        pydantic.Field(alias="customerOptions"),
    ] = UNSET
    r"""List of customer options from the list of customer records on the accounting software."""

    selected_customer_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="selectedCustomerId")
    ] = UNSET
    r"""Selected customer id from the list of customer records on the accounting software."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["customerOptions", "selectedCustomerId"]
        nullable_fields = ["customerOptions", "selectedCustomerId"]
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
