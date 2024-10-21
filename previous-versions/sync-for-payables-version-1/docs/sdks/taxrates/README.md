# TaxRates
(*tax_rates*)

## Overview

Get, create, and update Tax rates.

### Available Operations

* [get](#get) - Get tax rate
* [list](#list) - List all tax rates

## get

The *Get tax rate* endpoint returns a single tax rate for a given `taxRateId`.

[Tax rates](https://docs.codat.io/sync-for-payables-api#/schemas/TaxRate) are a set of taxes and associated rates within the SMB's accounting software.

Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=taxRates) for integrations that support getting a specific tax rate.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).


### Example Usage

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.tax_rates.get(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "tax_rate_id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetTaxRateRequest](../../models/operations/gettaxraterequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[shared.TaxRate](../../models/shared/taxrate.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorMessage                    | 401, 402, 403, 404, 409, 429, 500, 503 | application/json                       |
| errors.SDKError                        | 4XX, 5XX                               | \*/\*                                  |

## list

The *List tax rates* endpoint returns a list of [tax rates](https://docs.codat.io/sync-for-payables-api#/schemas/TaxRate) for a given company's connection.

[Tax rates](https://docs.codat.io/sync-for-payables-api#/schemas/TaxRate) are a set of taxes and associated rates within the SMB's accounting software.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.tax_rates.list(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "order_by": "-modifiedDate",
    "page": 1,
    "page_size": 100,
    "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListTaxRatesRequest](../../models/operations/listtaxratesrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[shared.TaxRates](../../models/shared/taxrates.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| errors.ErrorMessage                         | 400, 401, 402, 403, 404, 409, 429, 500, 503 | application/json                            |
| errors.SDKError                             | 4XX, 5XX                                    | \*/\*                                       |