from __future__ import annotations
import dataclasses
import dateutil.parser
from datetime import datetime
from marshmallow import fields
from typing import Optional


@dataclasses.dataclass
class DownloadFilesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadFilesQueryParams:
    date_: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'date', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class DownloadFilesSecurity:
    api_key: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class DownloadFilesRequest:
    path_params: DownloadFilesPathParams = dataclasses.field()
    query_params: DownloadFilesQueryParams = dataclasses.field()
    security: DownloadFilesSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DownloadFilesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    