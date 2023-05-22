# reports

## Overview

Reports

### Available Operations

* [get_aged_creditors_report](#get_aged_creditors_report) - Aged creditors report
* [get_aged_debtors_report](#get_aged_debtors_report) - Aged debtors report
* [get_balance_sheet](#get_balance_sheet) - Get balance sheet
* [get_cash_flow_statement](#get_cash_flow_statement) - Get cash flow statement
* [get_profit_and_loss](#get_profit_and_loss) - Get profit and loss
* [is_aged_creditors_report_available](#is_aged_creditors_report_available) - Aged creditors report available
* [is_aged_debtor_report_available](#is_aged_debtor_report_available) - Aged debtors report available

## get_aged_creditors_report

Returns aged creditors report for company that shows the total balance owed by a business to its suppliers over time.

### Example Usage

```python
import codataccounting
import dateutil.parser
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetAgedCreditorsReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=12,
    period_length_days=30,
    report_date=dateutil.parser.parse('2022-12-31').date(),
)

res = s.reports.get_aged_creditors_report(req)

if res.aged_creditor_report is not None:
    # handle response
```

## get_aged_debtors_report

Returns aged debtors report for company that shows the total outstanding balance due from customers to the business over time.

### Example Usage

```python
import codataccounting
import dateutil.parser
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.GetAgedDebtorsReportRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    number_of_periods=12,
    period_length_days=30,
    report_date=dateutil.parser.parse('2022-12-31').date(),
)

res = s.reports.get_aged_debtors_report(req)

if res.aged_debtor_report is not None:
    # handle response
```

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
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='ducimus',
)

res = s.reports.get_balance_sheet(req)

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
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='nemo',
)

res = s.reports.get_cash_flow_statement(req)

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
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
    period_length=4,
    periods_to_compare=20,
    start_month='illo',
)

res = s.reports.get_profit_and_loss(req)

if res.profit_and_loss_report is not None:
    # handle response
```

## is_aged_creditors_report_available

Indicates whether the aged creditor report is available for the company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.IsAgedCreditorsReportAvailableRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.reports.is_aged_creditors_report_available(req)

if res.is_aged_creditors_report_available_200_application_json_boolean is not None:
    # handle response
```

## is_aged_debtor_report_available

Indicates whether the aged debtor report is available for the company.

### Example Usage

```python
import codataccounting
from codataccounting.models import operations

s = codataccounting.CodatAccounting(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)

req = operations.IsAgedDebtorReportAvailableRequest(
    company_id='8a210b68-6988-11ed-a1eb-0242ac120002',
)

res = s.reports.is_aged_debtor_report_available(req)

if res.is_aged_debtor_report_available_200_application_json_boolean is not None:
    # handle response
```
