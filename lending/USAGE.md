<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_lending import CodatLending
from codat_lending.models import shared

with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as codat_lending:

    res = codat_lending.companies.create(request={
        "name": "Technicalium",
        "description": "Requested early access to the new financing scheme.",
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
from codat_lending import CodatLending
from codat_lending.models import shared

async def main():
    async with CodatLending(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as codat_lending:

        res = await codat_lending.companies.create_async(request={
            "name": "Technicalium",
            "description": "Requested early access to the new financing scheme.",
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->