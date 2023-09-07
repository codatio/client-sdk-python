# AccountBalance


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `available`                                     | *Optional[float]*                               | :heavy_minus_sign:                              | The account's current balance                   |                                                 |
| `currency`                                      | *Optional[str]*                                 | :heavy_minus_sign:                              | The currency of the account                     | GBP                                             |
| `pending`                                       | *Optional[float]*                               | :heavy_minus_sign:                              | Funds that are not yet available in the balance |                                                 |
| `reserved`                                      | *Optional[Any]*                                 | :heavy_minus_sign:                              | Funds reserved as holdings                      |                                                 |