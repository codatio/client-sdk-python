import dataclasses
from dataclasses_json import dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class UploadAttachmentPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    sync_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'syncId', 'style': 'simple', 'explode': False }})
    transaction_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'transactionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UploadAttachmentRequest:
    path_params: UploadAttachmentPathParams = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class UploadAttachment200ApplicationJSON:
    company_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('companyId') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    transaction_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transactionId') }})
    

@dataclasses.dataclass
class UploadAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    upload_attachment_200_application_json_object: Optional[UploadAttachment200ApplicationJSON] = dataclasses.field(default=None)
    