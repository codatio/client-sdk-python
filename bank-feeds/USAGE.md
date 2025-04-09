<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_bankfeeds import CodatBankFeeds
from codat_bankfeeds.models import shared


with CodatBankFeeds(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_bank_feeds:

    res = codat_bank_feeds.companies.create(request={
        "name": "Technicalium",
    })

    assert res is not None

    # Handle response
    print(res)
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
    ) as codat_bank_feeds:

        res = await codat_bank_feeds.companies.create_async(request={
            "name": "Technicalium",
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->