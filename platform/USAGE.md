<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_platform import CodatPlatform
from codat_platform.models import shared


with CodatPlatform(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
) as cp_client:

    res = cp_client.companies.add_product(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "product_identifier": "bank-feeds",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

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
    ) as cp_client:

        res = await cp_client.companies.add_product_async(request={
            "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
            "product_identifier": "bank-feeds",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->