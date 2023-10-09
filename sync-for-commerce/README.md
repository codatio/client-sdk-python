# Sync for Commerce

<!-- Start Codat Library Description -->
﻿Embedded accounting integrations for POS and eCommerce platforms.
<!-- End Codat Library Description -->

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install codat-sync-for-commerce
```
<!-- End SDK Installation -->

## Example Usage
<!-- Start SDK Example Usage -->


```python
import codatsynccommerce
from codatsynccommerce.models import shared

s = codatsynccommerce.CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = shared.CreateCompany(
    description='Requested early access to the new financing scheme.',
    name='Bank of Dave',
)

res = s.advanced_controls.create_company(req)

if res.company is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [AdvancedControls](docs/sdks/advancedcontrols/README.md)

* [create_company](docs/sdks/advancedcontrols/README.md#create_company) - Create company
* [get_configuration](docs/sdks/advancedcontrols/README.md#get_configuration) - Get company configuration
* [list_companies](docs/sdks/advancedcontrols/README.md#list_companies) - List companies
* [set_configuration](docs/sdks/advancedcontrols/README.md#set_configuration) - Set configuration

### [Connections](docs/sdks/connections/README.md)

* [create](docs/sdks/connections/README.md#create) - Create connection
* [get_sync_flow_url](docs/sdks/connections/README.md#get_sync_flow_url) - Start new sync flow
* [list](docs/sdks/connections/README.md#list) - List connections
* [update_authorization](docs/sdks/connections/README.md#update_authorization) - Update authorization
* [update_connection](docs/sdks/connections/README.md#update_connection) - Update connection

### [Integrations](docs/sdks/integrations/README.md)

* [get_branding](docs/sdks/integrations/README.md#get_branding) - Get branding for an integration
* [list](docs/sdks/integrations/README.md#list) - List integrations

### [Sync](docs/sdks/sync/README.md)

* [get](docs/sdks/sync/README.md#get) - Get sync status
* [get_last_successful_sync](docs/sdks/sync/README.md#get_last_successful_sync) - Last successful sync
* [get_latest_sync](docs/sdks/sync/README.md#get_latest_sync) - Latest sync status
* [get_status](docs/sdks/sync/README.md#get_status) - Get sync status
* [list](docs/sdks/sync/README.md#list) - List sync statuses
* [request](docs/sdks/sync/README.md#request) - Initiate new sync
* [request_for_date_range](docs/sdks/sync/README.md#request_for_date_range) - Initiate sync for specific range

### [SyncFlowSettings](docs/sdks/syncflowsettings/README.md)

* [get_config_text_sync_flow](docs/sdks/syncflowsettings/README.md#get_config_text_sync_flow) - Get preferences for text fields
* [get_visible_accounts](docs/sdks/syncflowsettings/README.md#get_visible_accounts) - List visible accounts
* [update_config_text_sync_flow](docs/sdks/syncflowsettings/README.md#update_config_text_sync_flow) - Update preferences for text fields
* [update_visible_accounts_sync_flow](docs/sdks/syncflowsettings/README.md#update_visible_accounts_sync_flow) - Update visible accounts