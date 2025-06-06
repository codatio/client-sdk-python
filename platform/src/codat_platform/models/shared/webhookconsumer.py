"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from codat_platform.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class WebhookConsumerTypedDict(TypedDict):
    r"""A webhook consumer is an HTTP endpoint that developers can configure to subscribe to Codat's supported event types.

    See our documentation for more details on [Codat's webhook service](https://docs.codat.io/using-the-api/webhooks/overview).

    """

    company_tags: NotRequired[Nullable[List[str]]]
    r"""Company tags provide an additional way to filter messages, independent of event types. Company tags are case-sensitive, and only messages from companies with matching tags will be sent to this endpoint. Use the format `tagKey:tagValue`."""
    disabled: NotRequired[Nullable[bool]]
    r"""Flag that enables or disables the endpoint from receiving events. Disabled when set to `true`."""
    event_types: NotRequired[List[str]]
    r"""An array of event types the webhook consumer subscribes to."""
    id: NotRequired[str]
    r"""Unique identifier for the webhook consumer."""
    url: NotRequired[str]
    r"""The URL that will consume webhook events dispatched by Codat."""


class WebhookConsumer(BaseModel):
    r"""A webhook consumer is an HTTP endpoint that developers can configure to subscribe to Codat's supported event types.

    See our documentation for more details on [Codat's webhook service](https://docs.codat.io/using-the-api/webhooks/overview).

    """

    company_tags: Annotated[
        OptionalNullable[List[str]], pydantic.Field(alias="companyTags")
    ] = UNSET
    r"""Company tags provide an additional way to filter messages, independent of event types. Company tags are case-sensitive, and only messages from companies with matching tags will be sent to this endpoint. Use the format `tagKey:tagValue`."""

    disabled: OptionalNullable[bool] = False
    r"""Flag that enables or disables the endpoint from receiving events. Disabled when set to `true`."""

    event_types: Annotated[Optional[List[str]], pydantic.Field(alias="eventTypes")] = (
        None
    )
    r"""An array of event types the webhook consumer subscribes to."""

    id: Optional[str] = None
    r"""Unique identifier for the webhook consumer."""

    url: Optional[str] = None
    r"""The URL that will consume webhook events dispatched by Codat."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["companyTags", "disabled", "eventTypes", "id", "url"]
        nullable_fields = ["companyTags", "disabled"]
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
