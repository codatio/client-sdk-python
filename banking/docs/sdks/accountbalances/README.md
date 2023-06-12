# account_balances

## Overview

Balances for a bank account including end-of-day batch balance or running balances per transaction.

### Available Operations

* [list](#list) - List account balances

## list

Gets a list of balances for a bank account including end-of-day batch balance or running balances per transaction.

### Example Usage

```python
import codatbanking
from codatbanking.models import operations

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.ListAccountBalancesRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='provident',
)

res = s.account_balances.list(req)

if res.account_balances is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListAccountBalancesRequest](../../models/operations/listaccountbalancesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.ListAccountBalancesResponse](../../models/operations/listaccountbalancesresponse.md)**

