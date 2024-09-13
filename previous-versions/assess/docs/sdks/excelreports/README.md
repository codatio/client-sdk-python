# ExcelReports
(*excel_reports*)

## Overview

Downloadable reports.

### Available Operations

* [generate_excel_report](#generate_excel_report) - Generate Excel report
* [get_accounting_marketing_metrics](#get_accounting_marketing_metrics) - Get marketing metrics report
* [get_excel_report](#get_excel_report) - Download Excel report
* [get_excel_report_generation_status](#get_excel_report_generation_status) - Get Excel report status

## generate_excel_report

Generate an Excel report which can subsequently be downloaded.

### Example Usage

```python
from codat_assess import CodatAssess
from codat_assess.models import shared

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.excel_reports.generate_excel_report(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "report_type": shared.ExcelReportType.ENHANCED_CASH_FLOW,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GenerateExcelReportRequest](../../models/operations/generateexcelreportrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[shared.ExcelStatus](../../models/shared/excelstatus.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## get_accounting_marketing_metrics

Get the marketing metrics from an accounting source for a given company.

Request an Excel report for download.

### Example Usage

```python
from codat_assess import CodatAssess
from codat_assess.models import shared

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.excel_reports.get_accounting_marketing_metrics(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    "number_of_periods": 495559,
    "period_length": 644039,
    "period_unit": shared.PeriodUnit.MONTH,
    "report_date": "29-09-2020",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAccountingMarketingMetricsRequest](../../models/operations/getaccountingmarketingmetricsrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[shared.Report](../../models/shared/report.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## get_excel_report

Download the previously generated Excel report to a local drive.

### Example Usage

```python
from codat_assess import CodatAssess
from codat_assess.models import shared

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.excel_reports.get_excel_report(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "report_type": shared.ExcelReportType.ENHANCED_CASH_FLOW,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetExcelReportRequest](../../models/operations/getexcelreportrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## get_excel_report_generation_status

Returns the status of the latest report requested.

### Example Usage

```python
from codat_assess import CodatAssess
from codat_assess.models import shared

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.excel_reports.get_excel_report_generation_status(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "report_type": shared.ExcelReportType.ENHANCED_INVOICES,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetExcelReportGenerationStatusRequest](../../models/operations/getexcelreportgenerationstatusrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[shared.ExcelStatus](../../models/shared/excelstatus.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
