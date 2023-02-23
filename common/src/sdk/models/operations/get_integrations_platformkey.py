import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetIntegrationsPlatformKeyPathParams:
    platform_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'platformKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetIntegrationsPlatformKeyRequest:
    path_params: GetIntegrationsPlatformKeyPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrationsPlatformKey404ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried') }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId') }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode') }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error') }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service') }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrationsPlatformKey401ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried') }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId') }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode') }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error') }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service') }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode') }})
    
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


@dataclass_json
@dataclasses.dataclass
class GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeatures:
    feature_state: GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeaturesFeatureStateEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureState') }})
    feature_type: GetIntegrationsPlatformKeyIntegrationDatatypeFeatureSupportedFeaturesFeatureTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureType') }})
    

@dataclass_json
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


@dataclass_json
@dataclasses.dataclass
class GetIntegrationsPlatformKeyIntegration:
    r"""GetIntegrationsPlatformKeyIntegration
    An integration that Codat supports
    """
    
    enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    logo_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('logoUrl') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    data_provided_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataProvidedBy') }})
    datatype_features: Optional[list[GetIntegrationsPlatformKeyIntegrationDatatypeFeature]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatypeFeatures') }})
    integration_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    is_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBeta') }})
    is_offline_connector: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isOfflineConnector') }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    source_type: Optional[GetIntegrationsPlatformKeyIntegrationSourceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType') }})
    

@dataclasses.dataclass
class GetIntegrationsPlatformKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_integrations_platform_key_401_application_json_object: Optional[GetIntegrationsPlatformKey401ApplicationJSON] = dataclasses.field(default=None)
    get_integrations_platform_key_404_application_json_object: Optional[GetIntegrationsPlatformKey404ApplicationJSON] = dataclasses.field(default=None)
    integration: Optional[GetIntegrationsPlatformKeyIntegration] = dataclasses.field(default=None)
    