"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountCategoriesUpdatedWebhookData:
    
    modified_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modifiedDate'), 'exclude': lambda f: f is None }})
    r"""The date on which this account categories were last modified in Codat."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountCategoriesUpdatedWebhook:
    r"""Webhook request body for account categories updated."""
    
    alert_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alertId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the webhook event."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for your client in Codat."""
    client_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clientName'), 'exclude': lambda f: f is None }})
    r"""Name of your client in Codat."""
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('companyId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for your SMB in Codat."""
    data: Optional[AccountCategoriesUpdatedWebhookData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    data_connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataConnectionId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for a company's data connection."""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""A human readable message about the webhook."""
    rule_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ruleId'), 'exclude': lambda f: f is None }})
    r"""Unique identifier for the rule."""
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""The type of rule."""
    