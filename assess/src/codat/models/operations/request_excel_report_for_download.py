from __future__ import annotations
import dataclasses
import dateutil.parser
import requests as requests_http
from codat import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class RequestExcelReportForDownloadReportTypeEnum(str, Enum):
    AUDIT = "audit"


@dataclasses.dataclass
class RequestExcelReportForDownloadRequest:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    report_type: RequestExcelReportForDownloadReportTypeEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'reportType', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RequestExcelReportForDownload200ApplicationJSON:
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errorMessage'), 'exclude': lambda f: f is None }})
    file_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fileSize'), 'exclude': lambda f: f is None }})
    in_progress: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inProgress'), 'exclude': lambda f: f is None }})
    last_generated: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastGenerated'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    last_invocation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastInvocationId'), 'exclude': lambda f: f is None }})
    queued: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('queued'), 'exclude': lambda f: f is None }})
    report_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportType'), 'exclude': lambda f: f is None }})
    success: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class RequestExcelReportForDownloadResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    request_excel_report_for_download_200_application_json_object: Optional[RequestExcelReportForDownload200ApplicationJSON] = dataclasses.field(default=None)
    