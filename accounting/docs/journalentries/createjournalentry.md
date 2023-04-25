# create_journal_entry
Available in: `journal_entries`

Posts a new journalEntry to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create journal entry model](https://docs.codat.io/accounting-api#/operations/get-create-journalEntries-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=journalEntries) for integrations that support creating journal entries.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateJournalEntryRequest(
    journal_entry=shared.JournalEntry(
        created_on="2022-10-23T00:00:00Z",
        description="mollitia",
        id="a30b7b91-449a-4e69-8088-d418bb71804f",
        journal_lines=[
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="23d54393-5f37-47ac-9c9b-7e93b6a3c523",
                    name="Sharon Hayes",
                ),
                currency="impedit",
                description="dolor",
                net_amount=3078.67,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="deserunt",
                            id="b0ecb812-a661-4489-84a8-e9085075bc25",
                        ),
                        shared.InvoiceTo(
                            data_type="dolorem",
                            id="8253343f-b0a4-4e66-aa47-578d171e2941",
                        ),
                        shared.InvoiceTo(
                            data_type="totam",
                            id="18fc679b-6b2f-4253-99b8-55d015b62c8b",
                        ),
                        shared.InvoiceTo(
                            data_type="praesentium",
                            id="3a38a8a8-8c14-4420-8c2c-aeb1ae1ecf8c",
                        ),
                    ],
                ),
            ),
            shared.JournalLine(
                account_ref=shared.AccountRef(
                    id="34946bba-7a05-4a8b-8a9e-c5b3688cca36",
                    name="Sara Kuhic",
                ),
                currency="iure",
                description="sit",
                net_amount=8973.52,
                tracking=shared.Propertiestracking2(
                    record_refs=[
                        shared.InvoiceTo(
                            data_type="vel",
                            id="6e97e054-1033-447d-b8ff-2491145fab9e",
                        ),
                        shared.InvoiceTo(
                            data_type="veniam",
                            id="9a4af336-664e-4aa6-bf2f-f14e8c1b352a",
                        ),
                        shared.InvoiceTo(
                            data_type="porro",
                            id="cedacc52-2781-44ec-a016-bc41ea1342d4",
                        ),
                    ],
                ),
            ),
        ],
        journal_ref=shared.JournalRef(
            id="104a25ef-71de-457a-91d6-14a4317692ea",
            name="Lena Howell",
        ),
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        posted_on="2022-10-23T00:00:00Z",
        record_ref=shared.InvoiceTo(
            data_type="vero",
            id="522b828a-9030-4660-b024-c79b4cc64c2b",
        ),
        source_modified_date="2022-10-23T00:00:00Z",
        supplemental_data=shared.SupplementalData(
            content={
                "culpa": {
                    "odit": "optio",
                },
            },
        ),
        updated_on="2022-10-23T00:00:00Z",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=287244,
)

res = s.journal_entries.create_journal_entry(req)

if res.create_journal_entry_response is not None:
    # handle response
```