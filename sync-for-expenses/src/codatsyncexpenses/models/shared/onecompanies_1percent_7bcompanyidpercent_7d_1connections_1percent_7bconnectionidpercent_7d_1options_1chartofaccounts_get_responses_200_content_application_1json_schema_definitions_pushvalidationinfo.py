"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushfieldvalidation as shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushfieldvalidation
from codatsyncexpenses import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1chartOfAccountsGetResponses200ContentApplication1jsonSchemaDefinitionsPushValidationInfo:
    information: Optional[list[shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushfieldvalidation.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1chartOfAccountsGetResponses200ContentApplication1jsonSchemaDefinitionsPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('information') }})
    warnings: Optional[list[shared_onecompanies_1percent_7bcompanyidpercent_7d_1connections_1percent_7bconnectionidpercent_7d_1options_1chartofaccounts_get_responses_200_content_application_1json_schema_definitions_pushfieldvalidation.Onecompanies1Percent7BcompanyIDPercent7D1connections1Percent7BconnectionIDPercent7D1options1chartOfAccountsGetResponses200ContentApplication1jsonSchemaDefinitionsPushFieldValidation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warnings') }})
    

