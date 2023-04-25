# get_integration
Available in: `integrations`

Get single integration, by platformKey

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetIntegrationRequest(
    platform_key="gbol",
)

res = s.integrations.get_integration(req)

if res.integration is not None:
    # handle response
```