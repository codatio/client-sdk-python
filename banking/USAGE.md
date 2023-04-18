<!-- Start SDK Example Usage -->
```python
import codatbanking
from codatbanking.models import operations, shared

s = codatbanking.CodatBanking(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListAccountBalancesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="corrupti",
)
    
res = s.account_balances.list_account_balances(req)

if res.account_balances is not None:
    # handle response
```
<!-- End SDK Example Usage -->