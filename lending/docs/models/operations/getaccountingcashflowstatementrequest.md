# GetAccountingCashFlowStatementRequest


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `company_id`                                      | *str*                                             | :heavy_check_mark:                                | Unique identifier for a company.                  | 8a210b68-6988-11ed-a1eb-0242ac120002              |
| `period_length`                                   | *int*                                             | :heavy_check_mark:                                | Number of months defining the period of interest. | 4                                                 |
| `periods_to_compare`                              | *int*                                             | :heavy_check_mark:                                | Number of periods with `periodLength` to compare. | 20                                                |
| `start_month`                                     | *Optional[str]*                                   | :heavy_minus_sign:                                | The month the report starts from.                 | 2022-10-23 00:00:00 +0000 UTC                     |