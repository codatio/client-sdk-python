# DataIntegrity
(*data_integrity*)

## Overview

Match mutable accounting data with immutable banking data to increase confidence in financial data.

### Available Operations

* [details](#details) - List data type data integrity
* [status](#status) - Get data integrity status
* [summary](#summary) - Get data integrity summary

## details

Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.

### Example Usage

```python
from codat_assess import CodatAssess
from codat_assess.models import shared

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.data_integrity.details(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "data_type": shared.DataIntegrityDataType.BANKING_ACCOUNTS,
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

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.ListDataTypeDataIntegrityDetailsRequest](../../models/operations/listdatatypedataintegritydetailsrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[shared.Details](../../models/shared/details.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |


## status

Gets match status for a given company and datatype.

### Example Usage

```python
from codat_assess import CodatAssess
from codat_assess.models import shared

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.data_integrity.status(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "data_type": shared.DataIntegrityDataType.BANKING_ACCOUNTS,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetDataIntegrityStatusRequest](../../models/operations/getdataintegritystatusrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[shared.Status](../../models/shared/status.md)**

### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.ErrorMessage         | 401,402,403,404,429,500,503 | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |


## summary

Gets match summary for a given company and datatype, optionally restricted by a Codat query string.

### Example Usage

```python
from codat_assess import CodatAssess
from codat_assess.models import shared

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.data_integrity.summary(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "data_type": shared.DataIntegrityDataType.BANKING_ACCOUNTS,
    "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetDataIntegritySummariesRequest](../../models/operations/getdataintegritysummariesrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[shared.Summaries](../../models/shared/summaries.md)**

### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.ErrorMessage             | 400,401,402,403,404,429,500,503 | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |
