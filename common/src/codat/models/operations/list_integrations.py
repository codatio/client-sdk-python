from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ListIntegrationsQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListIntegrationsRequest:
    query_params: ListIntegrationsQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrations401ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrations400ApplicationJSON:
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('canBeRetried'), 'exclude': lambda f: f is None }})
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('correlationId'), 'exclude': lambda f: f is None }})
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }})
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('service'), 'exclude': lambda f: f is None }})
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksLinks:
    current: ListIntegrationsLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    self: ListIntegrationsLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    next: Optional[ListIntegrationsLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[ListIntegrationsLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous'), 'exclude': lambda f: f is None }})
    
class ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeaturesFeatureStateEnum(str, Enum):
    RELEASE = "Release"
    BETA = "Beta"
    DEPRECATED = "Deprecated"
    NOT_SUPPORTED = "NotSupported"
    NOT_IMPLEMENTED = "NotImplemented"

class ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeaturesFeatureTypeEnum(str, Enum):
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
class ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeatures:
    feature_state: ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeaturesFeatureStateEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureState') }})
    feature_type: ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeaturesFeatureTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureType') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksIntegrationDatatypeFeature:
    r"""ListIntegrationsLinksIntegrationDatatypeFeature
    Describes support for a given datatype and associated operations
    """
    
    datatype: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatype') }})
    supported_features: list[ListIntegrationsLinksIntegrationDatatypeFeatureSupportedFeatures] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('supportedFeatures') }})
    
class ListIntegrationsLinksIntegrationSourceTypeEnum(str, Enum):
    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    COMMERCE = "Commerce"
    OTHER = "Other"
    UNKNOWN = "Unknown"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinksIntegration:
    r"""ListIntegrationsLinksIntegration
    An integration that Codat supports
    """
    
    enabled: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    logo_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('logoUrl') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    data_provided_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataProvidedBy'), 'exclude': lambda f: f is None }})
    datatype_features: Optional[list[ListIntegrationsLinksIntegrationDatatypeFeature]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatypeFeatures'), 'exclude': lambda f: f is None }})
    integration_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId'), 'exclude': lambda f: f is None }})
    is_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBeta'), 'exclude': lambda f: f is None }})
    is_offline_connector: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isOfflineConnector'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId'), 'exclude': lambda f: f is None }})
    source_type: Optional[ListIntegrationsLinksIntegrationSourceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListIntegrationsLinks:
    r"""ListIntegrationsLinks
    Codat's Paging Model
    """
    
    links: ListIntegrationsLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    results: Optional[list[ListIntegrationsLinksIntegration]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class ListIntegrationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[ListIntegrationsLinks] = dataclasses.field(default=None)
    list_integrations_400_application_json_object: Optional[ListIntegrations400ApplicationJSON] = dataclasses.field(default=None)
    list_integrations_401_application_json_object: Optional[ListIntegrations401ApplicationJSON] = dataclasses.field(default=None)
    