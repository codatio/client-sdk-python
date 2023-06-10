# excel_reports

## Overview

Downloadable reports

### Available Operations

* [generate_excel_report](#generate_excel_report) - Generate Excel report
* [get_accounting_marketing_metrics](#get_accounting_marketing_metrics) - Get marketing metrics report
* [get_excel_report](#get_excel_report) - Download Excel report
* [get_excel_report_generation_status](#get_excel_report_generation_status) - Get Excel report status

## generate_excel_report

Generate an Excel report which can subsequently be downloaded.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GenerateExcelReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportType.ENHANCED_CASH_FLOW,
)

res = s.excel_reports.generate_excel_report(req)

if res.excel_status is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GenerateExcelReportRequest](../../models/operations/generateexcelreportrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.GenerateExcelReportResponse](../../models/operations/generateexcelreportresponse.md)**


## get_accounting_marketing_metrics

Get the marketing metrics from an accounting source for a given company.

Request an Excel report for download.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountingMarketingMetricsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    include_display_names=False,
    number_of_periods=836079,
    period_length=71036,
    period_unit=shared.PeriodUnit.WEEK,
    report_date='29-09-2020',
    show_input_values=False,
)

res = s.excel_reports.get_accounting_marketing_metrics(req)

if res.report is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAccountingMarketingMetricsRequest](../../models/operations/getaccountingmarketingmetricsrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |


### Response

**[operations.GetAccountingMarketingMetricsResponse](../../models/operations/getaccountingmarketingmetricsresponse.md)**


## get_excel_report

Download the previously generated Excel report to a local drive.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetExcelReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportType.ASSESS,
)

res = s.excel_reports.get_excel_report(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetExcelReportRequest](../../models/operations/getexcelreportrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |


### Response

**[operations.GetExcelReportResponse](../../models/operations/getexcelreportresponse.md)**


## get_excel_report_generation_status

Returns the status of the latest report requested.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetExcelReportGenerationStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportType.ENHANCED_INVOICES,
)

res = s.excel_reports.get_excel_report_generation_status(req)

if res.excel_status is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetExcelReportGenerationStatusRequest](../../models/operations/getexcelreportgenerationstatusrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.GetExcelReportGenerationStatusResponse](../../models/operations/getexcelreportgenerationstatusresponse.md)**

