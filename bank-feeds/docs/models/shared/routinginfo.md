# RoutingInfo

Routing information for the bank. This does not include account number.


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `bank_code`                                                  | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | The numeric identifier of the routing number                 |
| `type`                                                       | [OptionalNullable[shared.Type]](../../models/shared/type.md) | :heavy_minus_sign:                                           | The type of routing number.                                  |