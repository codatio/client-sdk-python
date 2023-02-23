import dataclasses
from dataclasses_json import dataclass_json
from sdk import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingPathParams:
    platform_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'platformKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingRequest:
    path_params: GetIntegrationsPlatformKeyBrandingPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImageImage:
    r"""GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImageImage
    Image reference.
    """
    
    alt: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('alt') }})
    src: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('src') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImage:
    image: Optional[GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImageImage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('image') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingBrandingLogo:
    r"""GetIntegrationsPlatformKeyBrandingBrandingLogo
    Logo branding references.
    """
    
    full: Optional[GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('full') }})
    square: Optional[GetIntegrationsPlatformKeyBrandingBrandingLogoBrandingImage] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('square') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingBranding:
    button: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('button') }})
    logo: Optional[GetIntegrationsPlatformKeyBrandingBrandingLogo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logo') }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    

@dataclasses.dataclass
class GetIntegrationsPlatformKeyBrandingResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    branding: Optional[GetIntegrationsPlatformKeyBrandingBranding] = dataclasses.field(default=None)
    