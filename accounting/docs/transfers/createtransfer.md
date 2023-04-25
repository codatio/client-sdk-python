# create_transfer
Available in: `transfers`

Posts a new transfer to the accounting package for a given company.

Required data may vary by integration. To see what data to post, first call [Get create transfer model](https://docs.codat.io/accounting-api#/operations/get-create-transfers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=transfers) for integrations that support creating transfers.

## Example Usage
```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateTransferRequest(
    transfer=shared.Transfer(
        contact_ref=shared.TransferContactRef(
            data_type="quae",
            id="8b38f1b6-1a33-41a5-8dc1-0294f92fed93",
        ),
        date_="2022-10-23T00:00:00Z",
        deposited_record_refs=[
            "expedita",
            "mollitia",
            "quas",
        ],
        description="asperiores",
        from_=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id="71e2992c-20ee-4122-8ac3-adc647d240bc",
                name="Pamela Watsica",
            ),
            amount=5375.31,
            currency="explicabo",
        ),
        id="824ccc6a-2f0f-45b9-93cb-11a7687d3100",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="2022-10-23T00:00:00Z",
        source_modified_date="2022-10-23T00:00:00Z",
        supplemental_data=shared.SupplementalData(
            content={
                "deleniti": {
                    "sed": "cum",
                    "sint": "soluta",
                    "voluptatem": "repellendus",
                    "dignissimos": "quaerat",
                },
                "nisi": {
                    "quia": "dolorum",
                    "nihil": "quisquam",
                    "molestiae": "fugiat",
                    "ab": "debitis",
                },
                "dolorum": {
                    "voluptates": "quam",
                },
                "iste": {
                    "similique": "sint",
                    "nobis": "distinctio",
                    "earum": "veniam",
                    "maiores": "et",
                },
            },
        ),
        to=shared.TransferAccount(
            account_ref=shared.AccountRef(
                id="79f650b1-e707-4e7e-8396-713bacce072a",
                name="Ms. Taylor Jacobson IV",
            ),
            amount=8177.85,
            currency="magni",
        ),
        tracking_category_refs=[
            shared.TrackingCategoryRef(
                id="9c10c185-16fd-478b-a262-1272628fa503",
                name="Chester Cole",
            ),
            shared.TrackingCategoryRef(
                id="7e72b3a6-5024-4b15-bf9b-b6ef72a50871",
                name="Wade Medhurst",
            ),
        ],
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.transfers.create_transfer(req)

if res.create_transfer_response is not None:
    # handle response
```