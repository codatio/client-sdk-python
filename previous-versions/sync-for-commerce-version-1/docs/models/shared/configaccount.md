# ConfigAccount

G/L account object for configuration.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `account_options`                                           | List[[AccountOption](../../models/shared/accountoption.md)] | :heavy_minus_sign:                                          | Object containing account options.                          |
| `description_text`                                          | *Optional[str]*                                             | :heavy_minus_sign:                                          | Descriprtive text for sales configuration section.          |
| `label_text`                                                | *Optional[str]*                                             | :heavy_minus_sign:                                          | Label text for sales configuration section.                 |
| `required`                                                  | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Required section to be configured for sync.                 |
| `selected_account_id`                                       | *Optional[str]*                                             | :heavy_minus_sign:                                          | Selected account id from the list of available accounts.    |