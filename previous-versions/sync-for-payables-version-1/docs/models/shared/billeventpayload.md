# BillEventPayload


## Fields

| Field                                                                                                                     | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               | Example                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `bill`                                                                                                                    | [Optional[shared.Bill]](../../models/shared/bill.md)                                                                      | :heavy_minus_sign:                                                                                                        | ﻿Bills are invoices that represent the SMB's financial obligations to their supplier for a purchase of goods or services. |                                                                                                                           |
| `company_id`                                                                                                              | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Unique identifier for your SMB in Codat.                                                                                  | 8a210b68-6988-11ed-a1eb-0242ac120002                                                                                      |
| `connection_id`                                                                                                           | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Unique identifier for a company's data connection.                                                                        | 2e9d2c44-f675-40ba-8049-353bfcb5e171                                                                                      |
| `push_operation_key`                                                                                                      | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | Unique identifier for the push operation.                                                                                 | 2e9d2c44-f675-40ba-8049-353bfcb5e171                                                                                      |