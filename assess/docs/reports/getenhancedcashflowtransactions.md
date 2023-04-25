# get_enhanced_cash_flow_transactions
Available in: `reports`

The Enhanced Cash Flow Transactions endpoint provides a fully categorized list of banking transactions for a company. Accounts and transaction data are obtained from the company's banking data sources.

## Example Usage
```python
import codatassess
from codatassess.models import operations

s = codatassess.CodatAssess(
    security=shared.Security(
        auth_header="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetEnhancedCashFlowTransactionsRequest(
    company_id="8a210b68-6988-11ed-a1eb-0242ac120002",
    page=1,
    page_size=100,
    query="rem",
)

res = s.reports.get_enhanced_cash_flow_transactions(req)

if res.enhanced_cash_flow_transactions is not None:
    # handle response
```