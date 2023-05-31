# mapping_options

## Overview

Mapping options for a companies expenses.

### Available Operations

* [get_mapping_options](#get_mapping_options) - Mapping options

## get_mapping_options

Gets the expense mapping options for a companies accounting software

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetMappingOptionsRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.mapping_options.get_mapping_options(req)

if res.mapping_options is not None:
    # handle response
```
