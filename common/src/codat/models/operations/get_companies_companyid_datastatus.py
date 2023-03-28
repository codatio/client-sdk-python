"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetCompaniesCompanyIDDataStatusRequest:
    
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDDataStatusNotFound:
    r"""One or more of the resources you referenced could not be found.
    This might be because your company or data connection id is wrong, or was already deleted.
    """
    
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canBeRetried'), 'exclude': lambda f: f is None }})  
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})  
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})  
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})  
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})  
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDDataStatusUnauthorized:
    r"""Your API request was not properly authorized."""
    
    can_be_retried: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('canBeRetried'), 'exclude': lambda f: f is None }})  
    correlation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('correlationId'), 'exclude': lambda f: f is None }})  
    detailed_error_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailedErrorCode'), 'exclude': lambda f: f is None }})  
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})  
    service: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service'), 'exclude': lambda f: f is None }})  
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('statusCode'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDDataStatus200ApplicationJSONDataStatus:
    r"""Describes the state of data in the Codat cache for a company and data type"""
    
    current_status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentStatus') }})  
    data_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType') }})  
    last_successful_sync: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastSuccessfulSync') }})
    r"""In Codat's data model, dates and times are represented using the <a class=\"external\" href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\">ISO 8601 standard</a>. Date and time fields are formatted as strings; for example:
    
    ```
    2020-10-08T22:40:50Z
    2021-01-01T00:00:00
    ```
    
    
    
    When syncing data that contains `DateTime` fields from Codat, make sure you support the following cases when reading time information:
    
    - Coordinated Universal Time (UTC): `2021-11-15T06:00:00Z`
    - Unqualified local time: `2021-11-15T01:00:00`
    - UTC time offsets: `2021-11-15T01:00:00-05:00`
    
    > 📘 Time zones
    > 
    > Not all dates from Codat will contain information about time zones.  
    > Where it is not available from the underlying platform, Codat will return these as times local to the business whose data has been synced.
    """  
    latest_successful_sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latestSuccessfulSyncId'), 'exclude': lambda f: f is None }})  
    latest_sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latestSyncId'), 'exclude': lambda f: f is None }})  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetCompaniesCompanyIDDataStatus200ApplicationJSON:
    r"""OK"""
    
    data_type1: Optional[GetCompaniesCompanyIDDataStatus200ApplicationJSONDataStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType1'), 'exclude': lambda f: f is None }})
    r"""Describes the state of data in the Codat cache for a company and data type"""  
    data_type2: Optional[GetCompaniesCompanyIDDataStatus200ApplicationJSONDataStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataType2'), 'exclude': lambda f: f is None }})
    r"""Describes the state of data in the Codat cache for a company and data type"""  
    

@dataclasses.dataclass
class GetCompaniesCompanyIDDataStatusResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    get_companies_company_id_data_status_200_application_json_object: Optional[GetCompaniesCompanyIDDataStatus200ApplicationJSON] = dataclasses.field(default=None)
    r"""OK"""  
    not_found: Optional[GetCompaniesCompanyIDDataStatusNotFound] = dataclasses.field(default=None)
    r"""One or more of the resources you referenced could not be found.
    This might be because your company or data connection id is wrong, or was already deleted.
    """  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    unauthorized: Optional[GetCompaniesCompanyIDDataStatusUnauthorized] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""  
    