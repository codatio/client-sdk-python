# configuration

## Overview

Companies sync configuration.

### Available Operations

* [get_company_configuration](#get_company_configuration) - Get company configuration
* [save_company_configuration](#save_company_configuration) - Set company configuration

## get_company_configuration

Gets a companies expense sync configuration

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.GetCompanyConfigurationRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.get_company_configuration(req)

if res.company_configuration is not None:
    # handle response
```

## save_company_configuration

Sets a companies expense sync configuration

### Example Usage

```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="Basic BASE_64_ENCODED(API_KEY)",
    ),
)

req = operations.SaveCompanyConfigurationRequest(
    company_configuration=shared.CompanyConfiguration(
        bank_account=shared.BankAccount(
            id='32',
        ),
        customer=shared.Customer(
            id='142',
        ),
        supplier=shared.Supplier(
            id='124',
        ),
    ),
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.configuration.save_company_configuration(req)

if res.company_configuration is not None:
    # handle response
```
