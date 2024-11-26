<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_platform import CodatPlatform
from codat_platform.models import shared

with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as s:
    res = s.settings.create_api_key(request={
        "name": "azure-invoice-finance-processor",
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
from codat_platform import CodatPlatform
from codat_platform.models import shared

async def main():
    async with CodatPlatform(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    ) as s:
        res = await s.settings.create_api_key_async(request={
            "name": "azure-invoice-finance-processor",
        })

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->