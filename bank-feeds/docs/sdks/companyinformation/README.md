# CompanyInformation
(*company_information*)

## Overview

Get detailed information about a company from the underlying accounting software.

### Available Operations

* [get](#get) - Get company information

## get

Use the *Get company information* endpoint to return information about the company available from the underlying accounting software.

### Supported Integrations
| Integration           | Supported |
|-----------------------|-----------|
| Oracle NetSuite       | Yes       |
| Xero                  | Yes       |
| Exact                 | No        |
| FreeAgent             | No        |
| Sage                  | No        |
| QuickBooks Online     | No        |

### Example Usage

```python
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.company_information.get(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetCompanyInformationRequest](../../models/operations/getcompanyinformationrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[shared.CompanyInformation](../../models/shared/companyinformation.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrorMessage          | 400, 401, 402, 403, 404, 429 | application/json             |
| errors.ErrorMessage          | 500, 503                     | application/json             |
| errors.SDKError              | 4XX, 5XX                     | \*/\*                        |