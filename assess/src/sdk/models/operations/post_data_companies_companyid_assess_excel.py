from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcelPathParams:
    company_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'companyId', 'style': 'simple', 'explode': False }})
    
class PostDataCompaniesCompanyIDAssessExcelReportTypeEnum(str, Enum):
    AUDIT = "audit"


@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcelQueryParams:
    report_type: PostDataCompaniesCompanyIDAssessExcelReportTypeEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'reportType', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcelRequest:
    path_params: PostDataCompaniesCompanyIDAssessExcelPathParams = dataclasses.field()
    query_params: PostDataCompaniesCompanyIDAssessExcelQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcel200ApplicationJSON:
    error_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errorMessage'), 'exclude': lambda f: f is None }})
    file_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fileSize'), 'exclude': lambda f: f is None }})
    in_progress: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('inProgress'), 'exclude': lambda f: f is None }})
    last_generated: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastGenerated'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    last_invocation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lastInvocationId'), 'exclude': lambda f: f is None }})
    queued: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('queued'), 'exclude': lambda f: f is None }})
    report_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reportType'), 'exclude': lambda f: f is None }})
    success: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('success'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostDataCompaniesCompanyIDAssessExcelResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_data_companies_company_id_assess_excel_200_application_json_object: Optional[PostDataCompaniesCompanyIDAssessExcel200ApplicationJSON] = dataclasses.field(default=None)
    