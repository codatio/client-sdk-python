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
    
res = s.categories.get_data_assess_accounts_categories()

if res.get_data_assess_accounts_categories_chart_of_account_category_all_ofs is not None:
    # handle response
```
<!-- End SDK Example Usage -->