# ExcelReports
(*excel_reports*)

## Overview

Download reports in Excel format.

### Available Operations

* [download](#download) - Download Excel report
* [generate](#generate) - Generate Excel report
* [get_status](#get_status) - Get Excel report status

## download

﻿The *Download Excel report* endpoint downloads the latest successfully generated Excel report of a specified report type for a given company. 

The downloadable Excel file is returned in the response. You can save it to your local machine.

You can [learn more](https://docs.codat.io/lending/features/excel-download-overview#feature-components) about valid Excel report types.

### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.excel_reports.download(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "report_type": shared.ExcelReportTypes.ENHANCED_FINANCIALS,
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DownloadExcelReportRequest](../../models/operations/downloadexcelreportrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[bytes](../../models/.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## generate

The *Generate Excel report* endpoint requests the production of a downloadable Excel file for a report type specified in the `reportType` query parameter.

In response, the endpoint returns the [status](https://docs.codat.io/lending-api#/schemas/ExcelStatus) detailing the current state of the report generation request.

### Report types

| reportType                                                                           | Description                                                                                                                                   |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `audit`                          | Identifies inaccurate or out-of-date accounts, helping you to make decisions with confidence.                                                   || [audit](https://docs.codat.io/lending/excel/audit-report)                            | Identify inaccurate or out-of-date accounts, helping you to make decisions with confidence.                                                   |
| `enhancedCashFlow`    | Provides a fully categorized list of bank transactions for a company, allowing lenders to accurately forecast a company's cash flow.  |
| `enhancedFinancials` | Supports decision-making using fully categorized financial statements to allow lenders to automate their underwriting processes.                |
| `enhancedInvoices`     | Helps verify that payments have been made against historic invoices. Great for invoice finance lenders.                                       |

[Learn more](https://docs.codat.io/lending/features/excel-download-overview#feature-components) about valid Excel report types.




### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.excel_reports.generate(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "report_type": shared.ExcelReportTypes.ENHANCED_INVOICES,
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

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## get_status

﻿The *Get Excel report status* returns the status of the report mostly recently requested for Excel generation. It does not return the status of any historical report requests. 

Poll this endpoint to check the progress of the report once you have requested its generation. This will not affect the generation of the report. 

When the report generation completes successfully, the `inProgress` property will be marked as `false` and the `success` field will be marked as `true`.

### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.excel_reports.get_status(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "report_type": shared.ExcelReportTypes.ENHANCED_CASH_FLOW,
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

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 400, 401, 402, 403, 404, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |