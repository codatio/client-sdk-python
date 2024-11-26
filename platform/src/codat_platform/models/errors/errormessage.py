"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform import utils
from codat_platform.models.shared import errorvalidation as shared_errorvalidation
from codat_platform.types import BaseModel, OptionalNullable, UNSET
import pydantic
from typing import Optional
from typing_extensions import Annotated


class ErrorMessageData(BaseModel):
    can_be_retried: Annotated[Optional[str], pydantic.Field(alias="canBeRetried")] = (
        None
    )
    r"""`True` if the error occurred transiently and can be retried."""

    correlation_id: Annotated[Optional[str], pydantic.Field(alias="correlationId")] = (
        None
    )
    r"""Unique identifier used to propagate to all downstream services and determine the source of the error."""

    detailed_error_code: Annotated[
        Optional[int], pydantic.Field(alias="detailedErrorCode")
    ] = None
    r"""Machine readable error code used to automate processes based on the code returned."""

    error: Optional[str] = None
    r"""A brief description of the error."""

    service: Optional[str] = None
    r"""Codat's service the returned the error."""

    status_code: Annotated[Optional[int], pydantic.Field(alias="statusCode")] = None
    r"""The HTTP status code returned by the error."""

    validation: OptionalNullable[shared_errorvalidation.ErrorValidation] = UNSET
    r"""A human-readable object describing validation decisions Codat has made. If an operation has failed because of validation errors, they will be detailed here."""


class ErrorMessage(Exception):
    r"""Your API request was not properly authorized."""

    data: ErrorMessageData

    def __init__(self, data: ErrorMessageData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ErrorMessageData)