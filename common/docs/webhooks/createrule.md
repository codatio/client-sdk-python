# create_rule
Available in: `webhooks`

Create a new webhook configuration

## Example Usage
```python
import codatcommon
from codatcommon.models import shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = shared.Rule(
    company_id="39b73b17-cc2e-429e-915d-71654e9dcd1e",
    id="ff89c50e-a719-4ef5-a182-9917e53927b6",
    notifiers=shared.RuleNotifiers(
        emails=[
            "info@client.com",
            "info@client.com",
            "info@client.com",
            "info@client.com",
        ],
        webhook="https://webhook.client.com",
    ),
    type="sapiente",
)

res = s.webhooks.create_rule(req)

if res.rule is not None:
    # handle response
```