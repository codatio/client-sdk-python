"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatplatform import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebhookConsumerPrototype:
    UNSET='__SPEAKEASY_UNSET__'
    company_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId'), 'exclude': lambda f: f is WebhookConsumerPrototype.UNSET }})
    r"""Unique identifier of the company to indicate company-specific events. The associated webhook consumer will receive events only for the specified ID."""
    disabled: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disabled'), 'exclude': lambda f: f is WebhookConsumerPrototype.UNSET }})
    r"""Flag that enables or disables the endpoint from receiving events. Disabled when set to `true`."""
    event_types: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eventTypes'), 'exclude': lambda f: f is None }})
    r"""An array of event types the webhook consumer subscribes to."""
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""The URL that will consume webhook events dispatched by Codat."""
    

