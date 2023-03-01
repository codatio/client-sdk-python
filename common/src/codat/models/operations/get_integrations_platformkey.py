from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class GetIntegrationsPlatformKeyPathParams:
    platform_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'platformKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetIntegrationsPlatformKeyRequest:
    path_params: GetIntegrationsPlatformKeyPathParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKey404ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKey401ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    
class GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeaturesFeatureStateEnum(str, Enum):
    RELEASE = "Release"
    BETA = "Beta"
    DEPRECATED = "Deprecated"
    NOT_SUPPORTED = "NotSupported"
    NOT_IMPLEMENTED = "NotImplemented"

class GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeaturesFeatureTypeEnum(str, Enum):
    GET = "Get"
    POST = "Post"
    CATEGORIZATION = "Categorization"
    DELETE = "Delete"
    PUT = "Put"
    GET_AS_PDF = "GetAsPdf"
    DOWNLOAD_ATTACHMENT = "DownloadAttachment"
    GET_ATTACHMENT = "GetAttachment"
    GET_ATTACHMENTS = "GetAttachments"
    UPLOAD_ATTACHMENT = "UploadAttachment"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeatures:
    feature_state: GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeaturesFeatureStateEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureState') }})
    feature_type: GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeaturesFeatureTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureType') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKeyIntegrationDatatypeFeature:
    r"""GetIntegrationsPlatformKeyIntegrationDatatypeFeature
    Describes support for a given datatype and associated operations
    """
    
    datatype: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatype') }})
    supported_features: list[GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeatures] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('supportedFeatures') }})
    
class GetIntegrationsPlatformKeyIntegrationSourceTypeEnum(str, Enum):
    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    COMMERCE = "Commerce"
    OTHER = "Other"
    UNKNOWN = "Unknown"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationsPlatformKeyIntegration:
    r"""GetIntegrationsPlatformKeyIntegration
    An integration that Codat supports
    """
    
    enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    logo_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('logoUrl') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    data_provided_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataProvidedBy'), 'exclude': lambda f: f is None }})
    datatype_features: Optional[list[GetIntegrationsPlatformKeyIntegrationDatatypeFeature]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatypeFeatures'), 'exclude': lambda f: f is None }})
    integration_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId'), 'exclude': lambda f: f is None }})
    is_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBeta'), 'exclude': lambda f: f is None }})
    is_offline_connector: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isOfflineConnector'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId'), 'exclude': lambda f: f is None }})
    source_type: Optional[GetIntegrationsPlatformKeyIntegrationSourceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetIntegrationsPlatformKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_integrations_platform_key_401_application_json_object: Optional[GetIntegrationsPlatformKey401ApplicationJSON] = dataclasses.field(default=None)
    get_integrations_platform_key_404_application_json_object: Optional[GetIntegrationsPlatformKey404ApplicationJSON] = dataclasses.field(default=None)
    integration: Optional[GetIntegrationsPlatformKeyIntegration] = dataclasses.field(default=None)
    