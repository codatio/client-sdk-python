<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_files import CodatFiles

s = CodatFiles(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

res = s.files.download_files(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "date_": "2022-10-23T00:00:00Z",
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
from codat_files import CodatFiles

async def main():
    s = CodatFiles(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    )
    res = await s.files.download_files_async(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "date_": "2022-10-23T00:00:00Z",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->