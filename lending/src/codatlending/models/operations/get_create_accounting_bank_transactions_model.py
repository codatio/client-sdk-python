"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errormessage as shared_errormessage
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptionchoice as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptionchoice
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptionproperty as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptionproperty
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptiontype as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptiontype
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushvalidationinfo as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushvalidationinfo
from codatlending import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional



@dataclasses.dataclass
class GetCreateAccountingBankTransactionsModelRequest:
    account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountId', 'style': 'simple', 'explode': False }})
    r"""Unique identifier for an account"""
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetCreateAccountingBankTransactionsModelPushOption:
    r"""Success"""
    display_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displayName') }})
    required: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('required') }})
    type: shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptiontype.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1bankAccounts1Percent7BaccountIDPercent7D1bankTransactionsGetResponses200ContentApplication1jsonSchemaDefinitionsPushOptionType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    options: Optional[list[shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptionchoice.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1bankAccounts1Percent7BaccountIDPercent7D1bankTransactionsGetResponses200ContentApplication1jsonSchemaDefinitionsPushOptionChoice]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    properties: Optional[dict[str, shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushoptionproperty.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1bankAccounts1Percent7BaccountIDPercent7D1bankTransactionsGetResponses200ContentApplication1jsonSchemaDefinitionsPushOptionProperty]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('properties'), 'exclude': lambda f: f is None }})
    validation: Optional[shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1bankaccounts_1percent_7baccountidpercent_7d_1banktransactions_get_responses_200_content_application_1json_schema_definitions_pushvalidationinfo.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1bankAccounts1Percent7BaccountIDPercent7D1bankTransactionsGetResponses200ContentApplication1jsonSchemaDefinitionsPushValidationInfo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetCreateAccountingBankTransactionsModelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_message: Optional[shared_errormessage.ErrorMessage] = dataclasses.field(default=None)
    r"""Your API request was not properly authorized."""
    push_option: Optional[GetCreateAccountingBankTransactionsModelPushOption] = dataclasses.field(default=None)
    r"""Success"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

