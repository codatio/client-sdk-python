import dataclasses
from ..shared import bankfeedbankaccount as shared_bankfeedbankaccount
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetBankFeedsPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBankFeedsSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetBankFeedsRequest:
    path_params: GetBankFeedsPathParams = dataclasses.field()
    security: GetBankFeedsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetBankFeedsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bank_feed_bank_accounts: Optional[list[shared_bankfeedbankaccount.BankFeedBankAccount]] = dataclasses.field(default=None)
    