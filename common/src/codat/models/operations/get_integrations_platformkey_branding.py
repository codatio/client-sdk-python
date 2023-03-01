from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingPathParams:
    platform_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'platformKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingRequest:
    path_params: GetIntegrationsPlatformKeyBrandingPathParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImageImage:
    r"""GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImageImage
    Image reference.
    """
    
    alt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alt'), 'exclude': lambda f: f is None }})
    src: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('src'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImage:
    image: Optional[GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImageImage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('image'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingBrandingLogo:
    r"""GetIntegrationsPlatformKeyBrandingBrandingLogo
    Logo branding references.
    """
    
    full: Optional[GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('full'), 'exclude': lambda f: f is None }})
    square: Optional[GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('square'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingBranding:
    button: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('button'), 'exclude': lambda f: f is None }})
    logo: Optional[GetIntegrationsPlatformKeyBrandingBrandingLogo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logo'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    branding: Optional[GetIntegrationsPlatformKeyBrandingBranding] = dataclasses.field(default=None)
    