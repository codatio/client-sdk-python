# get_webhook
Available in: `webhooks`

Get a single webhook

## Example Usage
```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetWebhookRequest(
    rule_id="7318949f-c008-4936-a8ff-10d7ab563fa6",
)

res = s.webhooks.get_webhook(req)

if res.rule is not None:
    # handle response
```