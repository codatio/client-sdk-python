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


class FeesSupplierTypedDict(TypedDict):
    selected_supplier_id: NotRequired[Nullable[str]]
    r"""Selected supplier id from the list of supplier records on the accounting software."""
    supplier_options: NotRequired[Nullable[List[ConfigurationOptionTypedDict]]]
    r"""List of supplier options from the list of supplier records on the accounting software."""


class FeesSupplier(BaseModel):
    selected_supplier_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="selectedSupplierId")
    ] = UNSET
    r"""Selected supplier id from the list of supplier records on the accounting software."""

    supplier_options: Annotated[
        OptionalNullable[List[ConfigurationOption]],
        pydantic.Field(alias="supplierOptions"),
    ] = UNSET
    r"""List of supplier options from the list of supplier records on the accounting software."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["selectedSupplierId", "supplierOptions"]
        nullable_fields = ["selectedSupplierId", "supplierOptions"]
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