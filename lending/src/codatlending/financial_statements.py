"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .financial_statements_accounts import FinancialStatementsAccounts
from .financial_statements_balance_sheet import FinancialStatementsBalanceSheet
from .financial_statements_cash_flow import FinancialStatementsCashFlow
from .financial_statements_profit_and_loss import FinancialStatementsProfitAndLoss
from .sdkconfiguration import SDKConfiguration

class FinancialStatements:
    accounts: FinancialStatementsAccounts
    balance_sheet: FinancialStatementsBalanceSheet
    cash_flow: FinancialStatementsCashFlow
    profit_and_loss: FinancialStatementsProfitAndLoss
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.accounts = FinancialStatementsAccounts(self.sdk_configuration)
        self.balance_sheet = FinancialStatementsBalanceSheet(self.sdk_configuration)
        self.cash_flow = FinancialStatementsCashFlow(self.sdk_configuration)
        self.profit_and_loss = FinancialStatementsProfitAndLoss(self.sdk_configuration)
        
    