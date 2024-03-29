"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .balance_sheet import BalanceSheet
from .cash_flow import CashFlow
from .codatlending_financial_statements_accounts import CodatLendingFinancialStatementsAccounts
from .profit_and_loss import ProfitAndLoss
from .sdkconfiguration import SDKConfiguration

class FinancialStatements:
    accounts: CodatLendingFinancialStatementsAccounts
    balance_sheet: BalanceSheet
    cash_flow: CashFlow
    profit_and_loss: ProfitAndLoss
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.accounts = CodatLendingFinancialStatementsAccounts(self.sdk_configuration)
        self.balance_sheet = BalanceSheet(self.sdk_configuration)
        self.cash_flow = CashFlow(self.sdk_configuration)
        self.profit_and_loss = ProfitAndLoss(self.sdk_configuration)
        
    