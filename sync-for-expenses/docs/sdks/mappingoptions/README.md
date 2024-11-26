# MappingOptions
(*mapping_options*)

## Overview

Get accounts, trackingCategories and taxRates that can be used in your create and update requests.

### Available Operations

* [get_mapping_options](#get_mapping_options) - Mapping options

## get_mapping_options

Gets the mapping options (accounts, trackingCategories and taxRates) for a company's accounting software

### Example Usage

```python
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared

with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.mapping_options.get_mapping_options(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetMappingOptionsRequest](../../models/operations/getmappingoptionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[shared.MappingOptions](../../models/shared/mappingoptions.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.ErrorMessage               | 401, 402, 403, 404, 429, 500, 503 | application/json                  |
| errors.SDKError                   | 4XX, 5XX                          | \*/\*                             |