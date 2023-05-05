# integrations

## Overview

View useful information about codat's integrations.

### Available Operations

* [get_integration_branding](#get_integration_branding) - Get branding for an integration
* [list_integrations](#list_integrations) - List information on Codat's supported integrations

## get_integration_branding

Retrieve Integration branding assets.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetIntegrationBrandingRequest(
    platform_key='quibusdam',
)

res = s.integrations.get_integration_branding(req)

if res.branding is not None:
    # handle response
```

## list_integrations

Retrieve a list of available integrations support by datatype and state of release.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.ListIntegrationsRequest(
    order_by='-modifiedDate',
    page=1,
    page_size=100,
    query='unde',
)

res = s.integrations.list_integrations(req)

if res.integrations is not None:
    # handle response
```
