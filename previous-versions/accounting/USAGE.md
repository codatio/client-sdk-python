<!-- Start SDK Example Usage [usage] -->
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetAccountTransactionRequest(
    account_transaction_id='string',
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    connection_id='2e9d2c44-f675-40ba-8049-353bfcb5e171',
)

res = s.account_transactions.get(req)

if res.account_transaction is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->