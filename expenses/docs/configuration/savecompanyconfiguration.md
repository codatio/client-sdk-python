# save_company_configuration
Available in: `configuration`

Sets a companies expense sync configuration

## Example Usage
```python
import codatsyncexpenses
from codatsyncexpenses.models import operations, shared

s = codatsyncexpenses.CodatSyncExpenses(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.SaveCompanyConfigurationRequest(
    company_configuration=shared.CompanyConfiguration(
        bank_account=shared.BankAccount(
            id="32",
        ),
        customer=shared.Customer(
            id="142",
        ),
        supplier=shared.Supplier(
            id="124",
        ),
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.configuration.save_company_configuration(req)

if res.company_configuration is not None:
    # handle response
```