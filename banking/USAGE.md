<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListBankingAccountBalancesRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="unde",
)
    
res = s.account_balances.list_banking_account_balances(req)

if res.list_banking_account_balances_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->