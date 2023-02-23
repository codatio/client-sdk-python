import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetIntegrationsQueryParams:
    page: int = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetIntegrationsRequest:
    query_params: GetIntegrationsQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinksCurrent:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinksSelf:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinks:
    current: Optional[GetIntegrations200ApplicationJSONLinksCurrent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    next: Optional[GetIntegrations200ApplicationJSONLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next') }})
    previous: Optional[GetIntegrations200ApplicationJSONLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous') }})
    self: Optional[GetIntegrations200ApplicationJSONLinksSelf] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONResultsDatatypeFeaturesSupportedFeatures:
    feature_state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureState') }})
    feature_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureType') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONResultsDatatypeFeatures:
    datatype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatype') }})
    supported_features: Optional[list[GetIntegrations200ApplicationJSONResultsDatatypeFeaturesSupportedFeatures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supportedFeatures') }})
    
class GetIntegrations200ApplicationJSONResultsSourceTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    ACCOUNTING = "Accounting"
    BANKING = "Banking"
    BANK_FEED = "BankFeed"
    COMMERCE = "Commerce"
    EXPENSE = "Expense"
    OTHER = "Other"

class GetIntegrations200ApplicationJSONResultsSupportedEnvironmentsEnum(str, Enum):
    UNKNOWN = "Unknown"
    SANDBOX_ONLY = "SandboxOnly"
    LIVE_ONLY = "LiveOnly"
    LIVE_AND_SANDBOX = "LiveAndSandbox"


@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONResults:
    datatype_features: Optional[list[GetIntegrations200ApplicationJSONResultsDatatypeFeatures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatypeFeatures') }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    integration_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    is_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBeta') }})
    is_offline_connector: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isOfflineConnector') }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    linked_connections_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkedConnectionsCount') }})
    logo_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logoUrl') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    source_type: Optional[GetIntegrations200ApplicationJSONResultsSourceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType') }})
    supported_environments: Optional[GetIntegrations200ApplicationJSONResultsSupportedEnvironmentsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supportedEnvironments') }})
    total_connections_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalConnectionsCount') }})
    

@dataclass_json
@dataclasses.dataclass
class GetIntegrations200ApplicationJSON:
    r"""GetIntegrations200ApplicationJSON
    Used to represent what can be returned by an endpoint that supports paging.
    Usable with the [ProducesResponseType] attribute on a controller action.
    """
    
    links: Optional[GetIntegrations200ApplicationJSONLinks] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    results: Optional[list[GetIntegrations200ApplicationJSONResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    total_results: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    

@dataclasses.dataclass
class GetIntegrationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_integrations_200_application_json_object: Optional[GetIntegrations200ApplicationJSON] = dataclasses.field(default=None)
    