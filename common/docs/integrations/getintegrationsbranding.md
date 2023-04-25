# get_integrations_branding
Available in: `integrations`

Get branding for platform.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetIntegrationsBrandingRequest(
    platform_key="gbol",
)

res = s.integrations.get_integrations_branding(req)

if res.branding is not None:
    # handle response
```