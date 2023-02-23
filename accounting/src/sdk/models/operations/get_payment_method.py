import dataclasses
import dateutil.parser
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetPaymentMethodPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    payment_method_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'paymentMethodId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetPaymentMethodSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetPaymentMethodRequest:
    path_params: GetPaymentMethodPathParams = dataclasses.field()
    security: GetPaymentMethodSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetPaymentMethodSourceModifiedDateMetadata:
    is_deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('isDeleted') }})
    
class GetPaymentMethodSourceModifiedDateStatusEnum(str, Enum):
    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    ARCHIVED = "Archived"

class GetPaymentMethodSourceModifiedDateTypeEnum(str, Enum):
    UNKNOWN = "Unknown"
    CASH = "Cash"
    CHECK = "Check"
    CREDIT_CARD = "CreditCard"
    DEBIT_CARD = "DebitCard"
    BANK_TRANSFER = "BankTransfer"
    OTHER = "Other"


@dataclass_json
@dataclasses.dataclass
class GetPaymentMethodSourceModifiedDate:
    r"""GetPaymentMethodSourceModifiedDate
    > View the coverage for payment methods in the <a className=\"external\" href=\"https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=paymentMethods\" target=\"_blank\">Data coverage explorer</a>.
    
    ## Overview
    
    A Payment Method represents the payment method(s) used to pay a Bill. Payment Methods are referenced on [Bill Payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) and [Payments](https://docs.codat.io/accounting-api#/schemas/Payment).
    
    From the Payment Methods endpoints you can retrieve:
    
    - A list of all the Payment Methods used by a company: `GET/companies/{companyId}/data/paymentMethods`.
    - The details of an individual Payment Method:  
      `GET /companies/{companyId}/data/paymentMethods/{paymentMethodId}`.
    """
    
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    metadata: Optional[GetPaymentMethodSourceModifiedDateMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metadata') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    status: Optional[GetPaymentMethodSourceModifiedDateStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    type: Optional[GetPaymentMethodSourceModifiedDateTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclasses.dataclass
class GetPaymentMethodResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    source_modified_date: Optional[GetPaymentMethodSourceModifiedDate] = dataclasses.field(default=None)
    