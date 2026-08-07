# FinancialSummary

## Overview

View financial summary information for a company, including credit model reports and accounting score.

### Available Operations

* [download_credit_model_excel](#download_credit_model_excel) - Download credit model Excel
* [get_financial_summary](#get_financial_summary) - Get financial summary insights

## download_credit_model_excel

> **Available as beta release**
>
> This endpoint is part of a beta release. Please contact your account manager if you want to enable it.

Use the *Download Credit Model Excel* endpoint to download the credit model Excel file. 

Before using it, you must call the [Generate report](https://docs.codat.io/lending-api#/operations/generate-report) endpoint of type `creditModel`.

### Example Usage

<!-- UsageSnippet language="python" operationID="download-credit-model-excel" method="get" path="/companies/{companyId}/reports/creditModel/{reportId}/excel" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_summary.download_credit_model_excel(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "max_age": "2022-10-23T00:00:00Z",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.DownloadCreditModelExcelRequest](../../models/operations/downloadcreditmodelexcelrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[httpx.Response](../../models/data.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get_financial_summary

> **Available as beta release**
>
> This endpoint is part of a beta release. Please contact your account manager if you want to enable it.

Financial summary insights provide high-level indicators about the accuracy and completeness of a business’s financial data. These insights include:
- Closed Books Indicator – An estimate of the most recent accounting period officially closed by a business
- Accounting Score – An evaluation of the quality and completeness of a business’s bookkeeping

Before accessing this endpoint, you must call the [Generate report](https://docs.codat.io/lending-api#/operations/generate-report) endpoint of type `creditModel`.

> Please note that missing elements might be disabled for the account. Please contact account manager for more details.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-financial-summary" method="get" path="/companies/{companyId}/reports/creditModel/{reportId}/financialSummary" -->
```python
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.financial_summary.get_financial_summary(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetFinancialSummaryRequest](../../models/operations/getfinancialsummaryrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[shared.FinancialSummary](../../models/shared/financialsummary.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |