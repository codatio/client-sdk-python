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

    res = cl_client.accounting_bank_data.list_transactions(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
        "account_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
        "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
        "order_by": "-modifiedDate",
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

        res = await cl_client.accounting_bank_data.list_transactions_async(request={
            "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
            "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
            "account_id": "13d946f0-c5d5-42bc-b092-97ece17923ab",
            "query": "id=e3334455-1aed-4e71-ab43-6bccf12092ee",
            "order_by": "-modifiedDate",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->