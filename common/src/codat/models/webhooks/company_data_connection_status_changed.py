from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class CompanyDataConnectionStatusChangedResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    
class CompanyDataConnectionStatusChangedCompanyDataConnectionStatusChangedWebhookDataDataConnectionStatusEnum(str, Enum):
    PENDING_AUTH = "PendingAuth"
    LINKED = "Linked"
    UNLINKED = "Unlinked"
    DEAUTHORIZED = "Deauthorized"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompanyDataConnectionStatusChangedCompanyDataConnectionStatusChangedWebhookData:
    data_connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionId'), 'exclude': lambda f: f is None }})
    new_status: Optional[CompanyDataConnectionStatusChangedCompanyDataConnectionStatusChangedWebhookDataDataConnectionStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newStatus'), 'exclude': lambda f: f is None }})
    old_status: Optional[CompanyDataConnectionStatusChangedCompanyDataConnectionStatusChangedWebhookDataDataConnectionStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('oldStatus'), 'exclude': lambda f: f is None }})
    platform_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('platformKey'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompanyDataConnectionStatusChangedCompanyDataConnectionStatusChangedWebhook:
    r"""CompanyDataConnectionStatusChangedCompanyDataConnectionStatusChangedWebhook
    Webhook request body for a company's data connection status changed.
    """
    
    alert_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alertId'), 'exclude': lambda f: f is None }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    data: Optional[CompanyDataConnectionStatusChangedCompanyDataConnectionStatusChangedWebhookData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    rule_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleId'), 'exclude': lambda f: f is None }})
    rule_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleType'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CompanyDataConnectionStatusChangedRequest:
    request: Optional[CompanyDataConnectionStatusChangedCompanyDataConnectionStatusChangedWebhook] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    