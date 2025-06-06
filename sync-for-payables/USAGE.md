<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared

with CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_sync_payables:
    res = codat_sync_payables.companies.list(request={
        "page": 1,
        "page_size": 100,
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "order_by": "-modifiedDate",
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
from codat_sync_for_payables import CodatSyncPayables
from codat_sync_for_payables.models import shared

async def main():
    async with CodatSyncPayables(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_sync_payables:
        res = await codat_sync_payables.companies.list_async(request={
            "page": 1,
            "page_size": 100,
            "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
            "order_by": "-modifiedDate",
        })

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->