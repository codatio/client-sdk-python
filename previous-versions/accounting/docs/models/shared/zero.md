# Zero

Links the current record line to the underlying record line that created it. 

For example, if a bill is generated from a purchase order, this property allows you to connect the bill line item to the purchase order line item in our data model. 


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `data_type`                                                          | [Optional[shared.ZeroDataType]](../../models/shared/zerodatatype.md) | :heavy_minus_sign:                                                   | Allowed name of the 'dataType'.                                      |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | 'id' of the underlying record.                                       |
| `line_number`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Line number of the underlying record.                                |