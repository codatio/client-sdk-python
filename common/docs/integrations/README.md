# integrations

## Overview

View and manage your available integrations in Codat.

### Available Operations

* [get_integration](#get_integration) - Get integration
* [get_integrations_branding](#get_integrations_branding) - Get branding
* [list_integrations](#list_integrations) - List integrations

## get_integration

Get single integration, by platformKey

### Example Usage

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

## get_integrations_branding

Get branding for platform.

### Example Usage

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

## list_integrations

List your available integrations

### Example Usage

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
