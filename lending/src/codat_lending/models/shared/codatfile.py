"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_lending.types import BaseModel
from codat_lending.utils import FieldMetadata, MultipartFormMetadata
import io
import pydantic
from typing import IO, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class CodatFileTypedDict(TypedDict):
    content: Union[bytes, IO[bytes], io.BufferedReader]
    file_name: str
    content_type: NotRequired[str]


class CodatFile(BaseModel):
    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    file_name: Annotated[
        str, pydantic.Field(alias="fileName"), FieldMetadata(multipart=True)
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None
