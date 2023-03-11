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
   
req = operations.GetBankAccountPushOptionsRequest(
    path_params=operations.GetBankAccountPushOptionsPathParams(
        account_id="unde",
        company_id="deserunt",
        connection_id="porro",
    ),
    query_params=operations.GetBankAccountPushOptionsQueryParams(
        order_by="nulla",
        page=6027.63,
        page_size=8579.46,
        query="perspiciatis",
    ),
)
    
res = s.bank_account_transactions.get_bank_account_push_options(req)

if res.push_option is not None:
    # handle response
```
<!-- End SDK Example Usage -->