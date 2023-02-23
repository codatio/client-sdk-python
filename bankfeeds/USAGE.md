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
   
req = operations.GetBankAccountPushOptionsRequest(
    security=operations.GetBankAccountPushOptionsSecurity(
        api_key=shared.SchemeAPIKey(
            api_key="YOUR_API_KEY_HERE",
        ),
    ),
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