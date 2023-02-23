<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
s.config_security(
    security=shared.Security(
        api_key=shared.SchemeAPIKey(
            api_key="YOUR_API_KEY_HERE",
        ),
    )
)
   
req = operations.GetAccountTransactionRequest(
    security=operations.GetAccountTransactionSecurity(
        api_key=shared.SchemeAPIKey(
            api_key="YOUR_API_KEY_HERE",
        ),
    ),
    path_params=operations.GetAccountTransactionPathParams(
        account_transaction_id="unde",
        company_id="deserunt",
        connection_id="porro",
    ),
)
    
res = s.account_transactions.get_account_transaction(req)

if res.source_modified_date is not None:
    # handle response
```
<!-- End SDK Example Usage -->