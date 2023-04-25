# create_partner_expense_connection
Available in: `connections`

Creates a Partner Expense data connection

## Example Usage
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreatePartnerExpenseConnectionRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.connections.create_partner_expense_connection(req)

if res.data_connection is not None:
    # handle response
```