# suppliers

## Overview

Suppliers

### Available Operations

* [create_supplier](#create_supplier) - Create suppliers
* [download_supplier_attachment](#download_supplier_attachment) - Download supplier attachment
* [get_create_update_suppliers_model](#get_create_update_suppliers_model) - Get create/update supplier model
* [get_supplier](#get_supplier) - Get supplier
* [get_supplier_attachment](#get_supplier_attachment) - Get supplier attachment
* [list_supplier_attachments](#list_supplier_attachments) - List supplier attachments
* [list_suppliers](#list_suppliers) - List suppliers
* [put_supplier](#put_supplier) - Update supplier

## create_supplier

Push suppliers

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating suppliers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.CreateSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city="South Gavin",
                country="Saint Lucia",
                line1="explicabo",
                line2="expedita",
                postal_code="89844-4509",
                region="temporibus",
                type="Unknown",
            ),
            shared.Addressesitems(
                city="Blockview",
                country="Oman",
                line1="molestiae",
                line2="harum",
                postal_code="24520-2256",
                region="repellat",
                type="Billing",
            ),
            shared.Addressesitems(
                city="Jeniferton",
                country="Ukraine",
                line1="earum",
                line2="ipsa",
                postal_code="50506",
                region="dolores",
                type="Delivery",
            ),
        ],
        contact_name="culpa",
        default_currency="fugit",
        email_address="nemo",
        id="ee6c75af-8a60-4a7a-a346-e0979e5afe60",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="culpa",
        phone="776-533-8955 x34331",
        registration_number="deserunt",
        source_modified_date="iste",
        status="Archived",
        supplemental_data=shared.SupplementalData(
            content={
                "eveniet": {
                    "quae": "voluptates",
                    "impedit": "sunt",
                },
                "optio": {
                    "occaecati": "officia",
                    "consectetur": "excepturi",
                },
                "fuga": {
                    "ipsam": "fuga",
                    "magnam": "assumenda",
                    "nemo": "id",
                    "laboriosam": "nostrum",
                },
                "expedita": {
                    "fugiat": "exercitationem",
                    "veniam": "ea",
                },
            },
        ),
        supplier_name="aspernatur",
        tax_number="assumenda",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    timeout_in_minutes=587240,
)

res = s.suppliers.create_supplier(req)

if res.create_supplier_response is not None:
    # handle response
```

## download_supplier_attachment

Download supplier attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadSupplierAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.download_supplier_attachment(req)

if res.data is not None:
    # handle response
```

## get_create_update_suppliers_model

Get create/update supplier model. Returns the expected data for the request payload.

See the examples for integration-specific indicative models.

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support creating and updating suppliers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCreateUpdateSuppliersModelRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
)

res = s.suppliers.get_create_update_suppliers_model(req)

if res.push_option is not None:
    # handle response
```

## get_supplier

Gets a single supplier corresponding to the given ID.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSupplierRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.get_supplier(req)

if res.supplier is not None:
    # handle response
```

## get_supplier_attachment

Get supplier attachment

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSupplierAttachmentRequest(
    attachment_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.get_supplier_attachment(req)

if res.attachment is not None:
    # handle response
```

## list_supplier_attachments

Get supplier attachments

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSupplierAttachmentsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
)

res = s.suppliers.list_supplier_attachments(req)

if res.attachments_dataset is not None:
    # handle response
```

## list_suppliers

Gets the latest suppliers for a company, with pagination

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.ListSuppliersRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    order_by="-modifiedDate",
    page=1,
    page_size=100,
    query="expedita",
)

res = s.suppliers.list_suppliers(req)

if res.suppliers is not None:
    # handle response
```

## put_supplier

Push supplier

Required data may vary by integration. To see what data to post, first call [Get create/update supplier model](https://docs.codat.io/accounting-api#/operations/get-create-update-suppliers-model).

> **Supported Integrations**
> 
> Check out our [Knowledge UI](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=suppliers) for integrations that support updating suppliers.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations, shared

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.PutSupplierRequest(
    supplier=shared.Supplier(
        addresses=[
            shared.Addressesitems(
                city="Missoula",
                country="Tuvalu",
                line1="eos",
                line2="facere",
                postal_code="97933",
                region="esse",
                type="Billing",
            ),
            shared.Addressesitems(
                city="New Sabrynachester",
                country="Malta",
                line1="quam",
                line2="ad",
                postal_code="16550-1516",
                region="enim",
                type="Unknown",
            ),
        ],
        contact_name="delectus",
        default_currency="magnam",
        email_address="illo",
        id="cf6796ed-3d72-44c1-8f58-1e98cce3f716",
        metadata=shared.Metadata(
            is_deleted=False,
        ),
        modified_date="aliquid",
        phone="286-282-6630",
        registration_number="optio",
        source_modified_date="ex",
        status="Archived",
        supplemental_data=shared.SupplementalData(
            content={
                "alias": {
                    "assumenda": "totam",
                    "minima": "explicabo",
                    "soluta": "ad",
                },
                "adipisci": {
                    "nesciunt": "eos",
                    "placeat": "blanditiis",
                    "cumque": "dignissimos",
                },
                "placeat": {
                    "eligendi": "esse",
                },
                "quasi": {
                    "accusamus": "inventore",
                },
            },
        ),
        supplier_name="voluptas",
        tax_number="molestiae",
    ),
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    connection_id="2e9d2c44-f675-40ba-8049-353bfcb5e171",
    force_update=False,
    supplier_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    timeout_in_minutes=219664,
)

res = s.suppliers.put_supplier(req)

if res.put_supplier_200_application_json_object is not None:
    # handle response
```
