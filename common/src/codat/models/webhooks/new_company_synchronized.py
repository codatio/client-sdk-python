from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class NewCompanySynchronizedResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewCompanySynchronizedNewCompanySynchronizedWebhook:
    r"""NewCompanySynchronizedNewCompanySynchronizedWebhook
    Webhook request body to notify that a new company has successfully synchronized at least one dataType for the first time.
    """
    
    alert_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alertId'), 'exclude': lambda f: f is None }})
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId'), 'exclude': lambda f: f is None }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('message'), 'exclude': lambda f: f is None }})
    rule_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleId'), 'exclude': lambda f: f is None }})
    rule_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ruleType'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class NewCompanySynchronizedRequest:
    request: Optional[NewCompanySynchronizedNewCompanySynchronizedWebhook] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    