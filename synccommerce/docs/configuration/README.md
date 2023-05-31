# configuration

## Overview

Expressively configure preferences for any given Sync for Commerce company.

### Available Operations

* [get_configuration](#get_configuration) - Retrieve config preferences set for a company.
* [get_sync_status](#get_sync_status) - Get status for a company's syncs
* [set_configuration](#set_configuration) - Create or update configuration.

## get_configuration

Retrieve current config preferences.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetConfigurationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.get_configuration(req)

if res.configuration is not None:
    # handle response
```

## get_sync_status

Check the sync history and sync status for a company.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetSyncStatusRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.get_sync_status(req)

if res.status_code == 200:
    # handle response
```

## set_configuration

Make changes to configuration preferences.

### Example Usage

```python
import codatsynccommerce
from codatsynccommerce.models import operations

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.SetConfigurationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.set_configuration(req)

if res.configuration is not None:
    # handle response
```
