<!-- Start SDK Example Usage [usage] -->
```python
import codatsynccommerce
from codatsynccommerce.models import shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)


res = s.sync_flow_preferences.get_config_text_sync_flow()

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->