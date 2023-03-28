<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAccountTransactionRequest(
    account_transaction_id="unde",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)
    
res = s.account_transactions.get_account_transaction(req)

if res.source_modified_date is not None:
    # handle response
```
<!-- End SDK Example Usage -->