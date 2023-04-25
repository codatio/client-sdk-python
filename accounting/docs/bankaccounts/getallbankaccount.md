# get_all_bank_account
Available in: `bank_accounts`

Gets the bank account for given account ID.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAllBankAccountRequest(
    account_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    query="deserunt",
)

res = s.bank_accounts.get_all_bank_account(req)

if res.bank_statement_account is not None:
    # handle response
```