"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .clientratelimitresetwebhookdata import (
    ClientRateLimitResetWebhookData,
    ClientRateLimitResetWebhookDataTypedDict,
)
from codat_lending.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ClientRateLimitResetWebhookTypedDict(TypedDict):
    r"""Webhook request body for a client that has had their rate limit reset."""

    alert_id: NotRequired[str]
    r"""Unique identifier of the webhook event."""
    client_id: NotRequired[str]
    r"""Unique identifier for your client in Codat."""
    client_name: NotRequired[str]
    r"""Name of your client in Codat."""
    data: NotRequired[ClientRateLimitResetWebhookDataTypedDict]
    message: NotRequired[str]
    r"""A human-readable message about the webhook."""
    rule_id: NotRequired[str]
    r"""Unique identifier for the rule."""
    rule_type: NotRequired[str]
    r"""The type of rule."""


class ClientRateLimitResetWebhook(BaseModel):
    r"""Webhook request body for a client that has had their rate limit reset."""

    alert_id: Annotated[Optional[str], pydantic.Field(alias="AlertId")] = None
    r"""Unique identifier of the webhook event."""

    client_id: Annotated[Optional[str], pydantic.Field(alias="ClientId")] = None
    r"""Unique identifier for your client in Codat."""

    client_name: Annotated[Optional[str], pydantic.Field(alias="ClientName")] = None
    r"""Name of your client in Codat."""

    data: Annotated[
        Optional[ClientRateLimitResetWebhookData], pydantic.Field(alias="Data")
    ] = None

    message: Annotated[Optional[str], pydantic.Field(alias="Message")] = None
    r"""A human-readable message about the webhook."""

    rule_id: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible.",
            alias="RuleId",
        ),
    ] = None
    r"""Unique identifier for the rule."""

    rule_type: Annotated[Optional[str], pydantic.Field(alias="RuleType")] = None
    r"""The type of rule."""
