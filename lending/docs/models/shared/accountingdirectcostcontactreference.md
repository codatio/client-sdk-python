# AccountingDirectCostContactReference

A customer or supplier associated with the direct cost.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | Unique identifier for a customer or supplier.                                                        |
| `data_type`                                                                                          | [Optional[shared.AccountingDirectCostDataType]](../../models/shared/accountingdirectcostdatatype.md) | :heavy_minus_sign:                                                                                   | Allowed name of the 'dataType'.                                                                      |