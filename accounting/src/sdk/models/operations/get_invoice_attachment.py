import dataclasses
import dateutil.parser
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class GetInvoiceAttachmentPathParams:
    attachment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'attachmentId', 'style': 'simple', 'explode': False }})
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    invoice_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'invoiceId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetInvoiceAttachmentSecurity:
    api_key: shared_security.SchemeAPIKey = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetInvoiceAttachmentRequest:
    path_params: GetInvoiceAttachmentPathParams = dataclasses.field()
    security: GetInvoiceAttachmentSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetInvoiceAttachmentAttachment:
    content_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contentType') }})
    date_created: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dateCreated'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    file_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fileSize') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    include_when_sent: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('includeWhenSent') }})
    modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('modifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    source_modified_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sourceModifiedDate'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    

@dataclasses.dataclass
class GetInvoiceAttachmentResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    attachment: Optional[GetInvoiceAttachmentAttachment] = dataclasses.field(default=None)
    