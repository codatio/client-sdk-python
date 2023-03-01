<!-- Start SDK Example Usage -->
```python
import codatio
from codatio.models import operations, shared

s = codatio.Codatio()
s.config_security(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    )
)
   
req = operations.ListBankingAccountBalancesRequest(
    security=operations.ListBankingAccountBalancesSecurity(
        api_key="YOUR_API_KEY_HERE",
    ),
    path_params=operations.ListBankingAccountBalancesPathParams(
        company_id="unde",
        connection_id="deserunt",
    ),
    query_params=operations.ListBankingAccountBalancesQueryParams(
        order_by="porro",
        page=8442.66,
        page_size=6027.63,
        query="vero",
    ),
)
    
res = s.account_balances.list_banking_account_balances(req)

if res.links is not None:
    # handle response
```
<!-- End SDK Example Usage -->