import dataclasses
from ..shared import bankfeedbankaccount as shared_bankfeedbankaccount
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetBankFeedPathParams:
    bank_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'bankAccountId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBankFeedSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetBankFeedRequest:
    path_params: GetBankFeedPathParams = dataclasses.field()
    security: GetBankFeedSecurity = dataclasses.field()
    request: Optional[shared_bankfeedbankaccount.BankFeedBankAccount] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class GetBankFeedResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bank_feed_bank_account: Optional[shared_bankfeedbankaccount.BankFeedBankAccount] = dataclasses.field(default=None)
    