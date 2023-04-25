# financials

## Overview

Financials

### Available Operations

* [get_balance_sheet](#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](#get_cash_flow_statement) - Get cash flow statement
* [get_profit_and_loss](#get_profit_and_loss) - Get profit and loss

## get_balance_sheet

Gets the latest balance sheet for a company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetBalanceSheetRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    period_length=690865,
    periods_to_compare=125404,
    start_month="facere",
)

res = s.financials.get_balance_sheet(req)

if res.balance_sheet is not None:
    # handle response
```

## get_cash_flow_statement

Gets the latest cash flow statement for a company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetCashFlowStatementRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    period_length=170992,
    periods_to_compare=446583,
    start_month="repudiandae",
)

res = s.financials.get_cash_flow_statement(req)

if res.cash_flow_statement is not None:
    # handle response
```

## get_profit_and_loss

Gets the latest profit and loss for a company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetProfitAndLossRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    period_length=698306,
    periods_to_compare=457632,
    start_month="accusantium",
)

res = s.financials.get_profit_and_loss(req)

if res.profit_and_loss_report is not None:
    # handle response
```
