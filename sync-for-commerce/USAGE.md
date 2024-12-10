<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

with CodatSyncCommerce(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_commerce:
    res = codat_sync_commerce.sync_flow_settings.get_config_text_sync_flow(request={
        "locale": shared.Locale.EN_US,
    })

    if res is not None:
        # handle response
        pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from codat_sync_for_commerce import CodatSyncCommerce
from codat_sync_for_commerce.models import shared

async def main():
    async with CodatSyncCommerce(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_commerce:
        res = await codat_sync_commerce.sync_flow_settings.get_config_text_sync_flow_async(request={
            "locale": shared.Locale.EN_US,
        })

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->