"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import reportcomponent as shared_reportcomponent
from ..shared import reportdimension as shared_reportdimension
from ..shared import reporterror as shared_reporterror
from ..shared import reportmeasure as shared_reportmeasure
from codatassess import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Report:
    r"""Assess reports follow a consistent structure. Reports contain four sections of information:
    
    1. Report definition information such as:
      a. The report info (e.g. enhanced_profit_and_loss).
      b. The display name of the report (e.g. Enhanced Profit and Loss).
    2. Information about the dimension contained in the reports such as:
      a. The type of dimension (e.g. datetime, recordRef).
      b. The display name of the dimension (e.g. Period, Category type, Category sub type).
      c. The details about each item within the dimension (e.g. displayName:\"Jan 2022\", start:\"...\", end:\"...\", id:\"...\", name:\"...\").
    3. Information about the measures contained in the report such as:
      a. The display name of the measure (e.g. value of account, percentage change).
      b. The type of the measure (e.g. currency, percentage).
      c. The unit of the measure (e.g. %, GBP).
    4. The data for the report. When the *includeDisplayName* parameter is set to *true*, it shows the *dimensionDisplayName* and *itemDisplayName* to make the data human-readable. The default setting for *includeDisplayName* is *false*.
    
    Reports can be rendered as follows (ordering is implicit rather than explicit):
    
    ![A table showing an example of how a report can be rendered](https://files.readme.io/1fa20ca-Report1.png)
    
    # Data model
    
    ## Dimensions
    """
    
    dimensions: Optional[list[shared_reportdimension.ReportDimension]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimensions'), 'exclude': lambda f: f is None }})

    errors: Optional[list[shared_reporterror.ReportError]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})

    measures: Optional[list[shared_reportmeasure.ReportMeasure]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('measures'), 'exclude': lambda f: f is None }})

    report_data: Optional[list[shared_reportcomponent.ReportComponent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportData'), 'exclude': lambda f: f is None }})

    report_info: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reportInfo'), 'exclude': lambda f: f is None }})

    