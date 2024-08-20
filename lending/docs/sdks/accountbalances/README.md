# AccountBalances
(*banking.account_balances*)

### Available Operations

* [list](#list) - List account balances

## list

The *List account balances* endpoint returns a list of [account balances](https://docs.codat.io/lending-api#/schemas/AccountBalance) for a given company's connection.

[Account balances](https://docs.codat.io/lending-api#/schemas/AccountBalance) are balances for a bank account, including end-of-day batch balance or running balances per transaction.

Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/lending-api#/operations/refresh-company-data).
    

### Example Usage

```python
from codat_lending import CodatLending
from codat_lending.models import shared

s = CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)


res = s.banking.account_balances.list(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
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

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.ListBankingAccountBalancesRequest](../../models/operations/listbankingaccountbalancesrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |


### Response

**[shared.BankingAccountBalances](../../models/shared/bankingaccountbalances.md)**
### Errors

| Error Object                        | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.ErrorMessage                 | 400,401,402,403,404,409,429,500,503 | application/json                    |
| errors.SDKError                     | 4xx-5xx                             | */*                                 |
