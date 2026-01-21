<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_lending import CodatLending
from codat_lending.models import shared


with CodatLending(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cl_client:

    res = cl_client.companies.create(request={
        "name": "Technicalium",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

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
    ) as cl_client:

        res = await cl_client.companies.create_async(request={
            "name": "Technicalium",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->