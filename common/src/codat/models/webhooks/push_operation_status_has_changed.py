from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class PushOperationStatusHasChangedResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PushOperationStatusHasChangedPushOperationStatusChangedWebhookData:
    data_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataType'), 'exclude': lambda f: f is None }})
    push_operation_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pushOperationKey'), 'exclude': lambda f: f is None }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PushOperationStatusHasChangedPushOperationStatusChangedWebhook:
    r"""PushOperationStatusHasChangedPushOperationStatusChangedWebhook
    Webhook request body for a push operation status change.
    """
    
    alert_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alertId'), 'exclude': lambda f: f is None }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    data: Optional[PushOperationStatusHasChangedPushOperationStatusChangedWebhookData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    rule_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleId'), 'exclude': lambda f: f is None }})
    rule_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleType'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PushOperationStatusHasChangedRequest:
    request: Optional[PushOperationStatusHasChangedPushOperationStatusChangedWebhook] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    