# list_rules
Available in: `webhooks`

List webhooks that you are subscribed to.

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListRulesRequest(
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="architecto",
)

res = s.webhooks.list_rules(req)

if res.rules is not None:
    # handle response
```