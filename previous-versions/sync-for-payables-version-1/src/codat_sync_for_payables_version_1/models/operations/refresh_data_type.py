"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_sync_for_payables_version_1.models.shared import (
    schema_datatype as shared_schema_datatype,
)
from codat_sync_for_payables_version_1.types import BaseModel
from codat_sync_for_payables_version_1.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RefreshDataTypeRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    data_type: shared_schema_datatype.SchemaDataType
    r"""The key of a Codat data type"""
    connection_id: NotRequired[str]
    r"""Optionally, provide a data connection id to only queue pull operations on that connection."""


class RefreshDataTypeRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    data_type: Annotated[
        shared_schema_datatype.SchemaDataType,
        pydantic.Field(alias="dataType"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The key of a Codat data type"""

    connection_id: Annotated[
        Optional[str],
        pydantic.Field(alias="connectionId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optionally, provide a data connection id to only queue pull operations on that connection."""
