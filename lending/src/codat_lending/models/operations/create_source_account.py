"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.models.shared import (
    sourceaccount as shared_sourceaccount,
    sourceaccountprototype as shared_sourceaccountprototype,
    sourceaccountv2 as shared_sourceaccountv2,
    sourceaccountv2prototype as shared_sourceaccountv2prototype,
)
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


CreateSourceAccountRequestBodyTypedDict = TypeAliasType(
    "CreateSourceAccountRequestBodyTypedDict",
    Union[
        shared_sourceaccountprototype.SourceAccountPrototypeTypedDict,
        shared_sourceaccountv2prototype.SourceAccountV2PrototypeTypedDict,
    ],
)


CreateSourceAccountRequestBody = TypeAliasType(
    "CreateSourceAccountRequestBody",
    Union[
        shared_sourceaccountprototype.SourceAccountPrototype,
        shared_sourceaccountv2prototype.SourceAccountV2Prototype,
    ],
)


class CreateSourceAccountRequestTypedDict(TypedDict):
    company_id: str
    r"""Unique identifier for a company."""
    connection_id: str
    r"""Unique identifier for a connection."""
    request_body: NotRequired[CreateSourceAccountRequestBodyTypedDict]


class CreateSourceAccountRequest(BaseModel):
    company_id: Annotated[
        str,
        pydantic.Field(alias="companyId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a company."""

    connection_id: Annotated[
        str,
        pydantic.Field(alias="connectionId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier for a connection."""

    request_body: Annotated[
        Optional[CreateSourceAccountRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


CreateSourceAccountResponseBodyTypedDict = TypeAliasType(
    "CreateSourceAccountResponseBodyTypedDict",
    Union[
        shared_sourceaccount.SourceAccountTypedDict,
        shared_sourceaccountv2.SourceAccountV2TypedDict,
    ],
)
r"""Success"""


CreateSourceAccountResponseBody = TypeAliasType(
    "CreateSourceAccountResponseBody",
    Union[shared_sourceaccount.SourceAccount, shared_sourceaccountv2.SourceAccountV2],
)
r"""Success"""
