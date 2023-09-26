# DataIntegrity

## Overview

Match mutable accounting data with immutable banking data to increase confidence in financial data

### Available Operations

* [details](#details) - List data type data integrity
* [status](#status) - Get data integrity status
* [summary](#summary) - Get data integrity summary

## details

Gets record-by-record match results for a given company and datatype, optionally restricted by a Codat query string.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListDataTypeDataIntegrityDetailsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataType.BANKING_ACCOUNTS,
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='distinctio',
)

res = s.data_integrity.details(req)

if res.details is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.ListDataTypeDataIntegrityDetailsRequest](../../models/operations/listdatatypedataintegritydetailsrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |


### Response

**[operations.ListDataTypeDataIntegrityDetailsResponse](../../models/operations/listdatatypedataintegritydetailsresponse.md)**


## status

Gets match status for a given company and datatype.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDataIntegrityStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataType.BANKING_ACCOUNTS,
)

res = s.data_integrity.status(req)

if res.status is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetDataIntegrityStatusRequest](../../models/operations/getdataintegritystatusrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |


### Response

**[operations.GetDataIntegrityStatusResponse](../../models/operations/getdataintegritystatusresponse.md)**


## summary

Gets match summary for a given company and datatype, optionally restricted by a Codat query string.

### Example Usage

```python
import codatassess
from codatassess.models import operations, shared

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDataIntegritySummariesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    data_type=shared.DataIntegrityDataType.BANKING_ACCOUNTS,
    query='quibusdam',
)

res = s.data_integrity.summary(req)

if res.summaries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetDataIntegritySummariesRequest](../../models/operations/getdataintegritysummariesrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |


### Response

**[operations.GetDataIntegritySummariesResponse](../../models/operations/getdataintegritysummariesresponse.md)**

