# ReadData

## Overview

View validation outcomes for completed read data operations.

### Available Operations

* [get_validation_results](#get_validation_results) - Get validation results

## get_validation_results

Use the **Get validation results** endpoint to review warnings and errors encountered during the data type validation phase.

The validation result [schema](https://docs.codat.io/platform-api#/schemas/ValidationResult) contains two message arrays:

- **`warnings`** array lists potential issues with the data type that may require attention but don't block usage.
- **`errors`** array contains critical issues that must be resolved before the data type can be used.

### Example Usage

<!-- UsageSnippet language="python" operationID="get-read-validation-results" method="get" path="/companies/{companyId}/sync/{datasetId}/validation" example="Validation result" -->
```python
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.read_data.get_validation_results(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "dataset_id": "0812af6e-436a-491f-9056-db91cb961ad3",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetReadValidationResultsRequest](../../models/operations/getreadvalidationresultsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[shared.ValidationResult](../../models/shared/validationresult.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| errors.ErrorMessage     | 401, 402, 403, 404, 429 | application/json        |
| errors.ErrorMessage     | 500, 503                | application/json        |
| errors.SDKError         | 4XX, 5XX                | \*/\*                   |