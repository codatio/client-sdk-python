<!-- Start SDK Example Usage [usage] -->
```python
import codatsynccommerce
from codatsynccommerce.models import operations, shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigTextSyncFlowRequest(
    locale=shared.Locale.EN_US,
)

res = s.sync_flow_settings.get_config_text_sync_flow(req)

if res.localization_info is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->