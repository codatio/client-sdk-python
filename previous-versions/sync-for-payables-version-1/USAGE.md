<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

s = CodatSyncPayables(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.companies.create(request={
    "name": "Technicalium",
    "description": "Requested early access to the new financing scheme.",
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
from codat_sync_for_payables_version_1 import CodatSyncPayables
from codat_sync_for_payables_version_1.models import shared

async def main():
    s = CodatSyncPayables(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    )
    res = await s.companies.create_async(request={
        "name": "Technicalium",
        "description": "Requested early access to the new financing scheme.",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->