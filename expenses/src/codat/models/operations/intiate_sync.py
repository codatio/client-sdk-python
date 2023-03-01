from __future__ import annotations
import dataclasses
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class IntiateSyncPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IntiateSyncRequestBody:
    dataset_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('datasetIds') }})
    

@dataclasses.dataclass
class IntiateSyncRequest:
    path_params: IntiateSyncPathParams = dataclasses.field()
    request: Optional[IntiateSyncRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IntiateSync200ApplicationJSON:
    sync_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('syncId'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class IntiateSyncResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    intiate_sync_200_application_json_object: Optional[IntiateSync200ApplicationJSON] = dataclasses.field(default=None)
    