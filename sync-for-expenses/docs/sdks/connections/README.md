# connections

## Overview

Create and manage partner expense connection.

### Available Operations

* [create_partner_expense_connection](#create_partner_expense_connection) - Create Partner Expense connection

## create_partner_expense_connection

Creates a Partner Expense data connection

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.CreatePartnerExpenseConnectionRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.connections.create_partner_expense_connection(req)

if res.data_connection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.CreatePartnerExpenseConnectionRequest](../../models/operations/createpartnerexpenseconnectionrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |


### Response

**[operations.CreatePartnerExpenseConnectionResponse](../../models/operations/createpartnerexpenseconnectionresponse.md)**

