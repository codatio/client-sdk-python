# ManageData
(*manage_data*)

### Available Operations

* [get_status](#get_status) - Get data status

## get_status

Get the state of each data type for a company

### Example Usage

```python
import codatlending
from codatlending.models import operations, shared

s = codatlending.CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetDataStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.manage_data.get_status(req)

if res.data_statuses is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetDataStatusRequest](../../models/operations/getdatastatusrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |


### Response

**[operations.GetDataStatusResponse](../../models/operations/getdatastatusresponse.md)**

