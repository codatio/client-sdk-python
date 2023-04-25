# push_journal
Available in: `journals`

Posts a new journal to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create journal model](https://docs.codat.io/accounting-api#/operations/get-create-journals-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journals) for integrations that support creating journals.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.PushJournalRequest(
    journal=shared.Journal(
        created_on="2022-10-23T00:00:00Z",
        has_children=False,
        id="e62f6aa5-58a6-45e2-8830-16ca34bb87d4",
        journal_code="repellat",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        name="Lori Bergstrom",
        parent_id="culpa",
        source_modified_date="2022-10-23T00:00:00Z",
        status="Active",
        type="accusantium",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=461123,
)

res = s.journals.push_journal(req)

if res.push_journal_200_application_json_object is not None:
    # handle response
```