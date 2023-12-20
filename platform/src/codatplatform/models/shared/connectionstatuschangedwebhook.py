"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .connectionstatuschangedwebhookdata import ConnectionStatusChangedWebhookData
from codatplatform import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionStatusChangedWebhook:
    r"""Webhook request body for a company's data connection status changed."""
    alert_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('AlertId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the webhook event."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ClientId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for your client in Codat."""
    client_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ClientName'), 'exclude': lambda f: f is None }})
    r"""Name of your client in Codat."""
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('CompanyId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for your SMB in Codat."""
    data: Optional[ConnectionStatusChangedWebhookData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Data'), 'exclude': lambda f: f is None }})
    data_connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('DataConnectionId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for a company's data connection."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('Message'), 'exclude': lambda f: f is None }})
    r"""A human readable message about the webhook."""
    rule_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RuleId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the rule."""
    rule_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('RuleType'), 'exclude': lambda f: f is None }})
    r"""The type of rule."""
    

