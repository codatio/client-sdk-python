<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared

with CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.companies.create(request={
        "name": "Technicalium",
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
from codat_sync_for_expenses import CodatSyncExpenses
from codat_sync_for_expenses.models import shared

async def main():
    async with CodatSyncExpenses(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as s:
        res = await s.companies.create_async(request={
            "name": "Technicalium",
        })

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->