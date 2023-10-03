"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptionchoice as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptionchoice
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptionproperty as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptionproperty
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptiontype as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptiontype
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushvalidationinfo as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushvalidationinfo
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class GetCreateChartOfAccountsModelRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a company."""
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for a connection."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetCreateChartOfAccountsModelPushOption:
    r"""OK"""
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    r"""The property's display name."""
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    r"""The property is required if `True`."""
    type: shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptiontype.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1chartOfAccountsGetResponses200ContentApplication1jsonSchemaDefinitionsPushOptionType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The option type."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""A description of the property."""
    options: Optional[list[shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptionchoice.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1chartOfAccountsGetResponses200ContentApplication1jsonSchemaDefinitionsPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options') }})
    properties: Optional[dict[str, shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushoptionproperty.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1chartOfAccountsGetResponses200ContentApplication1jsonSchemaDefinitionsPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties') }})
    validation: Optional[shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushvalidationinfo.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1chartOfAccountsGetResponses200ContentApplication1jsonSchemaDefinitionsPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetCreateChartOfAccountsModelResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    push_option: Optional[GetCreateChartOfAccountsModelPushOption] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
