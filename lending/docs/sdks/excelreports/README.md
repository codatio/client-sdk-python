# excel_reports

## Overview

Downloadable reports

### Available Operations

* [download](#download) - Download Excel report
* [generate](#generate) - Generate Excel report
* [get_status](#get_status) - Get Excel report status

## download

﻿The *Download Excel report* endpoint downloads the latest successfully generated Excel report of a specified report type for a given company. 

The downloadable Excel file is returned in the response. You can save it to your local machine.

You can [learn more](https://docs.codat.io/lending/excel/overview) about valid Excel report types.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.DownloadExcelReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportTypes.ENHANCED_CASH_FLOW,
)

res = s.excel_reports.download(req)

if res.body is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DownloadExcelReportRequest](../../models/operations/downloadexcelreportrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.DownloadExcelReportResponse](../../models/operations/downloadexcelreportresponse.md)**


## generate

﻿The *Generate Excel report* endpoint requests the production of a downloadable Excel file for a report type specified in the `reportType` query parameter.

In response, the endpoint returns the [status](https://docs.codat.io/lending-api#/schemas/ExcelStatus) detailing the current state of the report generation request.

You can [learn more](https://docs.codat.io/lending/excel/overview) about valid Excel report types.





### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GenerateExcelReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportTypes.ENHANCED_INVOICES,
)

res = s.excel_reports.generate(req)

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


## get_status

﻿The *Get Excel report status* returns the status of the report mostly recently requested for Excel generation. It does not return the status of any historical report requests. 

Poll this endpoint to check the progress of the report once you have requested its generation. This will not affect the generation of the report. 

When the report generation completes successfully, the `inProgress` property will be marked as `false` and the `success` field will be marked as `true`.

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetExcelReportGenerationStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    report_type=shared.ExcelReportTypes.AUDIT,
)

res = s.excel_reports.get_status(req)

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
