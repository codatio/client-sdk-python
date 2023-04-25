# webhooks

## Overview

Manage webhooks, rules and alerts.

### Available Operations

* [create_rule](#create_rule) - Create webhook
* [get_webhook](#get_webhook) - Get webhook
* [list_rules](#list_rules) - List webhooks

## create_rule

Create a new webhook configuration

### Example Usage

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
        ],
        webhook="https://webhook.client.com",
    ),
    type="dolorem",
)

res = s.webhooks.create_rule(req)

if res.rule is not None:
    # handle response
```

## get_webhook

Get a single webhook

### Example Usage

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

## list_rules

List webhooks that you are subscribed to.

### Example Usage

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
    query="culpa",
)

res = s.webhooks.list_rules(req)

if res.rules is not None:
    # handle response
```
