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
    company_id="unde",
    connection_id="deserunt",
    order_by="porro",
    page=8442.66,
    page_size=6027.63,
    query="vero",
)
    
res = s.account_balances.list_banking_account_balances(req)

if res.links is not None:
    # handle response
```
<!-- End SDK Example Usage -->