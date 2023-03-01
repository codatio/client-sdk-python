from __future__ import annotations
import dataclasses
import dateutil.parser
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class CompaniesQueryParams:
    page: int = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CompaniesRequest:
    query_params: CompaniesQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSONLinksCurrent:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSONLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSONLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSONLinksSelf:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSONLinks:
    current: Optional[Companies200ApplicationJSONLinksCurrent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('current'), 'exclude': lambda f: f is None }})
    next: Optional[Companies200ApplicationJSONLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next'), 'exclude': lambda f: f is None }})
    previous: Optional[Companies200ApplicationJSONLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous'), 'exclude': lambda f: f is None }})
    self: Optional[Companies200ApplicationJSONLinksSelf] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('self'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSONResultsDataConnectionsDataConnectionErrors:
    errored_on_utc: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('erroredOnUtc'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    status_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusCode'), 'exclude': lambda f: f is None }})
    status_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('statusText'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSONResultsDataConnections:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    integration_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('integrationId') }})
    link_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('linkUrl') }})
    platform_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('platformName') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceId') }})
    created: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    data_connection_errors: Optional[list[Companies200ApplicationJSONResultsDataConnectionsDataConnectionErrors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnectionErrors'), 'exclude': lambda f: f is None }})
    last_sync: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastSync'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceType'), 'exclude': lambda f: f is None }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSONResults:
    data_connections: list[Companies200ApplicationJSONResultsDataConnections] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dataConnections') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    platform: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('platform') }})
    redirect: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('redirect') }})
    created: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    created_by_user_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('createdByUserName'), 'exclude': lambda f: f is None }})
    last_sync: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastSync'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Companies200ApplicationJSON:
    r"""Companies200ApplicationJSON
    Used to represent what can be returned by an endpoint that supports paging.
    Usable with the [ProducesResponseType] attribute on a controller action.
    """
    
    links: Optional[Companies200ApplicationJSONLinks] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links'), 'exclude': lambda f: f is None }})
    page_number: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber'), 'exclude': lambda f: f is None }})
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize'), 'exclude': lambda f: f is None }})
    results: Optional[list[Companies200ApplicationJSONResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results'), 'exclude': lambda f: f is None }})
    total_results: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CompaniesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    companies_200_application_json_object: Optional[Companies200ApplicationJSON] = dataclasses.field(default=None)
    