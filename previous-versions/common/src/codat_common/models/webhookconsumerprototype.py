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
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class WebhookConsumerPrototypeTypedDict(TypedDict):
    company_id: NotRequired[Nullable[str]]
    r"""Unique identifier of the company to indicate company-specific events. The associated webhook consumer will receive events only for the specified ID."""
    disabled: NotRequired[Nullable[bool]]
    r"""Flag that enables or disables the endpoint from receiving events. Disabled when set to `true`."""
    event_types: NotRequired[List[str]]
    r"""An array of event types the webhook consumer subscribes to."""
    url: NotRequired[str]
    r"""The URL that will consume webhook events dispatched by Codat."""


class WebhookConsumerPrototype(BaseModel):
    company_id: Annotated[OptionalNullable[str], pydantic.Field(alias="companyId")] = (
        UNSET
    )
    r"""Unique identifier of the company to indicate company-specific events. The associated webhook consumer will receive events only for the specified ID."""

    disabled: OptionalNullable[bool] = False
    r"""Flag that enables or disables the endpoint from receiving events. Disabled when set to `true`."""

    event_types: Annotated[Optional[List[str]], pydantic.Field(alias="eventTypes")] = (
        None
    )
    r"""An array of event types the webhook consumer subscribes to."""

    url: Optional[str] = None
    r"""The URL that will consume webhook events dispatched by Codat."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["companyId", "disabled", "eventTypes", "url"]
        nullable_fields = ["companyId", "disabled"]
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
