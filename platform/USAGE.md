<!-- Start SDK Example Usage [usage] -->
```python
import codatplatform
from codatplatform.models import shared

s = codatplatform.CodatPlatform(
    security=shared.Security(
        auth_header="<YOUR_API_KEY_HERE>",
    ),
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = s.settings.create_api_key(req)

if res.api_key_details is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->