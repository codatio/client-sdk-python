"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_common.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import Dict, List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class CustomDataTypeConfigurationTypedDict(TypedDict):
    r"""Client's configuration details for a specific custom data type and platform pair."""

    data_source: NotRequired[str]
    r"""Underlying endpoint of the source platform that will serve as a data source for the custom data type. This value is not validated by Codat."""
    key_by: NotRequired[List[str]]
    r"""An array of properties from the source system that can be used to uniquely identify the records returned for the custom data type. This value is not validated by Codat."""
    required_data: NotRequired[Dict[str, str]]
    r"""Properties required to be fetched from the underlying platform for the custom data type that is being configured. This value is not validated by Codat."""
    source_modified_date: NotRequired[Nullable[List[str]]]
    r"""Property in the source platform nominated by the client that defines the date when a record was last modified there. This value is not validated by Codat."""


class CustomDataTypeConfiguration(BaseModel):
    r"""Client's configuration details for a specific custom data type and platform pair."""

    data_source: Annotated[Optional[str], pydantic.Field(alias="dataSource")] = None
    r"""Underlying endpoint of the source platform that will serve as a data source for the custom data type. This value is not validated by Codat."""

    key_by: Annotated[Optional[List[str]], pydantic.Field(alias="keyBy")] = None
    r"""An array of properties from the source system that can be used to uniquely identify the records returned for the custom data type. This value is not validated by Codat."""

    required_data: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="requiredData")
    ] = None
    r"""Properties required to be fetched from the underlying platform for the custom data type that is being configured. This value is not validated by Codat."""

    source_modified_date: Annotated[
        OptionalNullable[List[str]], pydantic.Field(alias="sourceModifiedDate")
    ] = UNSET
    r"""Property in the source platform nominated by the client that defines the date when a record was last modified there. This value is not validated by Codat."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["dataSource", "keyBy", "requiredData", "sourceModifiedDate"]
        nullable_fields = ["sourceModifiedDate"]
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
