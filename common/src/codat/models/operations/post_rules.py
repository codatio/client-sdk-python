from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostRulesWebhookNotifiers:
    emails: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('emails'), 'exclude': lambda f: f is None }})
    webhook: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('webhook'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostRulesWebhook:
    r"""PostRulesWebhook
    Configuration to alert to a url or list of email addresses based on the given type / condition.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    notifiers: PostRulesWebhookNotifiers = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('notifiers') }})
    type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostRulesRequest:
    request: Optional[PostRulesWebhook] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostRules401ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostRulesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_rules_401_application_json_object: Optional[PostRules401ApplicationJSON] = dataclasses.field(default=None)
    webhook: Optional[PostRulesWebhook] = dataclasses.field(default=None)
    