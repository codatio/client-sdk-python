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
   
req = operations.GetBankFeedRequest(
    security=operations.GetBankFeedSecurity(
        api_key=shared.SchemeAPIKey(
            api_key="YOUR_API_KEY_HERE",
        ),
    ),
    path_params=operations.GetBankFeedPathParams(
        bank_account_id="unde",
        company_id="deserunt",
        connection_id="porro",
    ),
    request=shared.BankFeedBankAccount(
        account_name="nulla",
        account_number="id",
        account_type="vero",
        balance=5448.83,
        currency="nulla",
        feed_start_date="2022-09-21T19:40:56.584Z",
        id="fuga",
        modified_date="2022-07-02T16:51:57.664Z",
        sort_code="eum",
        status="iusto",
    ),
)
    
res = s.bank_feeds.get_bank_feed(req)

if res.bank_feed_bank_account is not None:
    # handle response
```
<!-- End SDK Example Usage -->