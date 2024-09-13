<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

s = CodatAccounting(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

res = s.account_transactions.get(request={
    "account_transaction_id": "<value>",
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
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
from codat_accounting import CodatAccounting
from codat_accounting.models import shared

async def main():
    s = CodatAccounting(
        security=shared.Security(
            auth_header="Basic BASE_64_ENCODED(API_KEY)",
        ),
    )
    res = await s.account_transactions.get_async(request={
        "account_transaction_id": "<value>",
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "connection_id": "2e9d2c44-f675-40ba-8049-353bfcb5e171",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->