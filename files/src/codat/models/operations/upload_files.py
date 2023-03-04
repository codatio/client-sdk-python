from __future__ import annotations
import dataclasses
import requests
from typing import Optional


@dataclasses.dataclass
class UploadFilesPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UploadFilesRequest:
    path_params: UploadFilesPathParams = dataclasses.field()
    

@dataclasses.dataclass
class UploadFilesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    