<!-- Start SDK Example Usage -->
```python
import codatcommon
from codatcommon.models import shared

s = codatcommon.CodatCommon(
    auth_header="",
)

req = shared.CreateAPIKey(
    name='azure-invoice-finance-processor',
)

res = s.settings.create_api_key(req)

if res.api_key_details is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->