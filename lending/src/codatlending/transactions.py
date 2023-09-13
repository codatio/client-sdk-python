"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from .transactions_account_transactions import TransactionsAccountTransactions
from .transactions_direct_costs import TransactionsDirectCosts
from .transactions_journal_entries import TransactionsJournalEntries
from .transactions_journals import TransactionsJournals
from .transactions_transfers import TransactionsTransfers

class Transactions:
    account_transactions: TransactionsAccountTransactions
    direct_costs: TransactionsDirectCosts
    journal_entries: TransactionsJournalEntries
    journals: TransactionsJournals
    transfers: TransactionsTransfers
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.account_transactions = TransactionsAccountTransactions(self.sdk_configuration)
        self.direct_costs = TransactionsDirectCosts(self.sdk_configuration)
        self.journal_entries = TransactionsJournalEntries(self.sdk_configuration)
        self.journals = TransactionsJournals(self.sdk_configuration)
        self.transfers = TransactionsTransfers(self.sdk_configuration)
        
    