<!-- Start SDK Example Usage -->
```python
import codat
from codat.models import operations, shared

s = codat.Codat()
s.config_security(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    )
)
   
req = operations.GetCreateUpdateAccountTransactionsModelRequest(
    path_params=operations.GetCreateUpdateAccountTransactionsModelPathParams(
        account_transaction_id="unde",
        company_id="deserunt",
        connection_id="porro",
    ),
)
    
res = s.account_transactions.get_create_update_account_transactions_model(req)

if res.source_modified_date is not None:
    # handle response
```
<!-- End SDK Example Usage -->