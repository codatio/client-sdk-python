# list_integrations
Available in: `integrations`

List your available integrations

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListIntegrationsRequest(
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="veritatis",
)

res = s.integrations.list_integrations(req)

if res.integrations is not None:
    # handle response
```