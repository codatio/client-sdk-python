from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSettingsProfile401ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSettingsProfileProfile:
    r"""GetSettingsProfileProfile
    Describes your Codat client instance
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    redirect_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('redirectUrl') }})
    alert_auth_header: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alertAuthHeader'), 'exclude': lambda f: f is None }})
    api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('apiKey'), 'exclude': lambda f: f is None }})
    confirm_company_name: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('confirmCompanyName'), 'exclude': lambda f: f is None }})
    icon_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('iconUrl'), 'exclude': lambda f: f is None }})
    logo_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logoUrl'), 'exclude': lambda f: f is None }})
    white_list_urls: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('whiteListUrls'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetSettingsProfileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_settings_profile_401_application_json_object: Optional[GetSettingsProfile401ApplicationJSON] = dataclasses.field(default=None)
    profile: Optional[GetSettingsProfileProfile] = dataclasses.field(default=None)
    