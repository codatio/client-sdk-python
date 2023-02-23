import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional

class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsDataTypeEnum(str, Enum):
    BANKING_ACCOUNTS = "banking-accounts"
    BANKING_TRANSACTIONS = "banking-transactions"
    BANK_ACCOUNTS = "bankAccounts"
    ACCOUNT_TRANSACTIONS = "accountTransactions"


@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    data_type: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsDataTypeEnum = dataclasses.field(metadata={'path_param': { 'field_name': 'dataType', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsQueryParams:
    page: float = dataclasses.field(metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    page_size: Optional[float] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsRequest:
    path_params: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsPathParams = dataclasses.field()
    query_params: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsQueryParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinksCurrent:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinksNext:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinksPrevious:
    href: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinksSelf:
    href: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('href') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinks:
    current: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinksCurrent = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current') }})
    self: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinksSelf = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('self') }})
    next: Optional[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinksNext] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next') }})
    previous: Optional[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinksPrevious] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksDataIntegrityDetailsMatches:
    amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionId') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    date_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksDataIntegrityDetails:
    amount: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('amount') }})
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connectionId') }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    matches: Optional[list[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksDataIntegrityDetailsMatches]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('matches') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinks:
    r"""GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinks
    Codat's Paging Model
    """
    
    links: GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksLinks = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('_links') }})
    page_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageNumber') }})
    page_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageSize') }})
    total_results: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('totalResults') }})
    results: Optional[list[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinksDataIntegrityDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    

@dataclasses.dataclass
class GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    links: Optional[GetDataCompaniesCompanyIDAssessDataTypesDataTypeDataIntegrityDetailsLinks] = dataclasses.field(default=None)
    