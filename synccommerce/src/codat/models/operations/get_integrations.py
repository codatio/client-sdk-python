from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
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
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinksCurrent:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinksSelf:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONLinks:
    current: Optional[GetIntegrations200ApplicationJSONLinksCurrent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('current'), 'exclude': lambda f: f is None }})
    next: Optional[GetIntegrations200ApplicationJSONLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[GetIntegrations200ApplicationJSONLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous'), 'exclude': lambda f: f is None }})
    self: Optional[GetIntegrations200ApplicationJSONLinksSelf] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('self'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONResultsDatatypeFeaturesSupportedFeatures:
    feature_state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureState'), 'exclude': lambda f: f is None }})
    feature_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('featureType'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONResultsDatatypeFeatures:
    datatype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatype'), 'exclude': lambda f: f is None }})
    supported_features: Optional[list[GetIntegrations200ApplicationJSONResultsDatatypeFeaturesSupportedFeatures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supportedFeatures'), 'exclude': lambda f: f is None }})
    
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSONResults:
    datatype_features: Optional[list[GetIntegrations200ApplicationJSONResultsDatatypeFeatures]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('datatypeFeatures'), 'exclude': lambda f: f is None }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled'), 'exclude': lambda f: f is None }})
    integration_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId'), 'exclude': lambda f: f is None }})
    is_beta: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isBeta'), 'exclude': lambda f: f is None }})
    is_offline_connector: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isOfflineConnector'), 'exclude': lambda f: f is None }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('key'), 'exclude': lambda f: f is None }})
    linked_connections_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkedConnectionsCount'), 'exclude': lambda f: f is None }})
    logo_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('logoUrl'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId'), 'exclude': lambda f: f is None }})
    source_type: Optional[GetIntegrations200ApplicationJSONResultsSourceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    supported_environments: Optional[GetIntegrations200ApplicationJSONResultsSupportedEnvironmentsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('supportedEnvironments'), 'exclude': lambda f: f is None }})
    total_connections_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalConnectionsCount'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrations200ApplicationJSON:
    r"""GetIntegrations200ApplicationJSON
    Used to represent what can be returned by an endpoint that supports paging.
    Usable with the [ProducesResponseType] attribute on a controller action.
    """
    
    links: Optional[GetIntegrations200ApplicationJSONLinks] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links'), 'exclude': lambda f: f is None }})
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber'), 'exclude': lambda f: f is None }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize'), 'exclude': lambda f: f is None }})
    results: Optional[list[GetIntegrations200ApplicationJSONResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    total_results: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetIntegrationsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_integrations_200_application_json_object: Optional[GetIntegrations200ApplicationJSON] = dataclasses.field(default=None)
    