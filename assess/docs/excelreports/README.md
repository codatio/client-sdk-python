# excel_reports

## Overview

Downloadable reports

### Available Operations

* [download_excel_report](#download_excel_report) - Download generated excel report
* [generate_excel_report](#generate_excel_report) - Generate an Excel report
* [get_accounting_marketing_metrics](#get_accounting_marketing_metrics) - Get the marketing metrics from an accounting source for a given company.
* [get_excel_report](#get_excel_report) - Download generated excel report
* [get_excel_report_generation_status](#get_excel_report_generation_status) - Get status of Excel report

## download_excel_report

Download the previously generated Excel report to a local drive.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadExcelReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportTypeEnum.AUDIT,
)

res = s.excel_reports.download_excel_report(req)

if res.body is not None:
    # handle response
```

## generate_excel_report

Generate an Excel report which can subsequently be downloaded.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GenerateExcelReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportTypeEnum.ASSESS,
)

res = s.excel_reports.generate_excel_report(req)

if res.excel_status is not None:
    # handle response
```

## get_accounting_marketing_metrics

Request an Excel report for download.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountingMarketingMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=739264,
    period_length=19987,
    period_unit=shared.PeriodUnitEnum.DAY,
    report_date='29-09-2020',
    show_input_values=False,
)

res = s.excel_reports.get_accounting_marketing_metrics(req)

if res.report is not None:
    # handle response
```

## get_excel_report

Download the previously generated Excel report to a local drive.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetExcelReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportTypeEnum.ASSESS,
)

res = s.excel_reports.get_excel_report(req)

if res.body is not None:
    # handle response
```

## get_excel_report_generation_status

Returns the status of the latest report requested.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetExcelReportGenerationStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportTypeEnum.ASSESS,
)

res = s.excel_reports.get_excel_report_generation_status(req)

if res.excel_status is not None:
    # handle response
```
