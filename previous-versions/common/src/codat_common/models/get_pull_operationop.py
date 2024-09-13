"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_common.types import BaseModel
from codat_common.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import TypedDict
from typing_extensions import Annotated


class GetPullOperationRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    dataset_id: str
    r"""Unique identifier for the dataset that completed its sync."""


class GetPullOperationRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    dataset_id: Annotated[
        str,
        pydantic.Field(alias="datasetId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for the dataset that completed its sync."""
