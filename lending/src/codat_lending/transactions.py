"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from codat_lending.account_transactions import AccountTransactions
from codat_lending.codatlending_direct_costs import CodatLendingDirectCosts
from codat_lending.codatlending_transfers import CodatLendingTransfers
from codat_lending.journal_entries import JournalEntries
from codat_lending.journals import Journals


class Transactions(BaseSDK):
    account_transactions: AccountTransactions
    direct_costs: CodatLendingDirectCosts
    transfers: CodatLendingTransfers
    journal_entries: JournalEntries
    journals: Journals

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.account_transactions = AccountTransactions(self.sdk_configuration)
        self.direct_costs = CodatLendingDirectCosts(self.sdk_configuration)
        self.transfers = CodatLendingTransfers(self.sdk_configuration)
        self.journal_entries = JournalEntries(self.sdk_configuration)
        self.journals = Journals(self.sdk_configuration)