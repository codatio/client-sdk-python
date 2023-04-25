# list_bank_accounts
Available in: `bank_accounts`

Gets the list of bank accounts for a given connection

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBankAccountsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="distinctio",
)

res = s.bank_accounts.list_bank_accounts(req)

if res.bank_accounts is not None:
    # handle response
```