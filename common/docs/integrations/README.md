# integrations

## Overview

View and manage your available integrations in Codat.

### Available Operations

* [get](#get) - Get integration
* [get_branding](#get_branding) - Get branding
* [list](#list) - List integrations

## get

Get single integration, by platformKey

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.GetIntegrationRequest(
    platform_key='gbol',
)

res = s.integrations.get(req)

if res.integration is not None:
    # handle response
```

## get_branding

Get branding for platform.

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.GetIntegrationsBrandingRequest(
    platform_key='gbol',
)

res = s.integrations.get_branding(req)

if res.branding is not None:
    # handle response
```

## list

List your available integrations

### Example Usage

```python
import codatcommon
from codatcommon.models import operations

s = codatcommon.CodatCommon(
    security=shared.Security(
        auth_header="",
    ),
)

req = operations.ListIntegrationsRequest(
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='suscipit',
)

res = s.integrations.list(req)

if res.integrations is not None:
    # handle response
```
