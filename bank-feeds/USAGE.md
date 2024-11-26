<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared

with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
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
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared

async def main():
    async with CodatBankFeeds(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as s:
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