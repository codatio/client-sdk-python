# webhooks

## Overview

Manage webhooks, rules, and events.

### Available Operations

* [create](#create) - Create webhook
* [get](#get) - Get webhook
* [list](#list) - List webhooks

## create

Create a new webhook configuration

### Example Usage

```python
import codatcommon
from codatcommon.models import shared

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)

req = shared.Rule(
    company_id='39b73b17-cc2e-429e-915d-71654e9dcd1e',
    id='ff89c50e-a719-4ef5-a182-9917e53927b6',
    notifiers=shared.RuleNotifiers(
        emails=[
            'info@client.com',
        ],
        webhook='https://webhook.client.com',
    ),
    type='reiciendis',
)

res = s.webhooks.create(req)

if res.rule is not None:
    # handle response
```

## get

Get a single webhook

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.GetWebhookRequest(
    rule_id='7318949f-c008-4936-a8ff-10d7ab563fa6',
)

res = s.webhooks.get(req)

if res.rule is not None:
    # handle response
```

## list

List webhooks that you are subscribed to.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.ListRulesRequest(
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='est',
)

res = s.webhooks.list(req)

if res.rules is not None:
    # handle response
```
