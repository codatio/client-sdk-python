# create_account
Available in: `accounts`

Creates a new account for a given company.

Required data may vary by integration. To see what data to post, first call [Get create account model](https://docs.codat.io/accounting-api#/operations/get-create-chartOfAccounts-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateAccountRequest(
    account=shared.Account(
        currency="quibusdam",
        current_balance=6027.63,
        description="nulla",
        fully_qualified_category="corrupti",
        fully_qualified_name="illum",
        id="69a674e0-f467-4cc8-b96e-d151a05dfc2d",
        is_bank_account=False,
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        name="Emilio Krajcik",
        nominal_code="esse",
        source_modified_date="2022-10-23T00:00:00Z",
        status="Archived",
        type="Liability",
        valid_datatype_links=[
            shared.ValidDataTypeLinks(
                links=[
                    "nam",
                ],
                property="officia",
            ),
            shared.ValidDataTypeLinks(
                links=[
                    "fugit",
                    "deleniti",
                    "hic",
                ],
                property="optio",
            ),
            shared.ValidDataTypeLinks(
                links=[
                    "beatae",
                    "commodi",
                    "molestiae",
                ],
                property="modi",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=186332,
)

res = s.accounts.create_account(req)

if res.create_account_response is not None:
    # handle response
```