# CompanyInformation

Information about the company from the underlying accounting software.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `base_currency`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Currency set in the accounting software of the linked company.      |
| `company_name`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Name of the linked company.                                         |
| `multicurrency_enabled`                                             | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | Boolean showing if the organisation has multicurrency enabled       |
| `plan_type`                                                         | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Accounting software subscription type such as Trial, Demo, Standard |