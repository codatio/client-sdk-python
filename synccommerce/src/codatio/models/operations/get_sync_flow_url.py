from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class GetSyncFlowURLPathParams:
    accounting_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'accountingKey', 'style': 'simple', 'explode': False }})
    commerce_key: str = dataclasses.field(metadata={'path_param': { 'field_name': 'commerceKey', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSyncFlowURLQueryParams:
    merchant_identifier: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'merchantIdentifier', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetSyncFlowURLRequest:
    path_params: GetSyncFlowURLPathParams = dataclasses.field()
    query_params: GetSyncFlowURLQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSyncFlowURLResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    