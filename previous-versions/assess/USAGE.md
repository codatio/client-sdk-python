<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from codat_assess import CodatAssess
from codat_assess.models import operations

s = CodatAssess(
    auth_header="Basic BASE_64_ENCODED(API_KEY)",
)

s.reports.generate_loan_summary(request={
    "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
    "source_type": operations.SourceType.ACCOUNTING,
})

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from codat_assess import CodatAssess
from codat_assess.models import operations

async def main():
    s = CodatAssess(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    )
    await s.reports.generate_loan_summary_async(request={
        "company_id": "8a210b68-6988-11ed-a1eb-0242ac120002",
        "source_type": operations.SourceType.ACCOUNTING,
    })
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->