"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from codat_lending.credit_notes import CreditNotes
from codat_lending.customers import Customers
from codat_lending.direct_incomes import DirectIncomes
from codat_lending.invoices import Invoices
from codat_lending.payments import Payments
from codat_lending.reports import Reports


class AccountsReceivable(BaseSDK):
    customers: Customers
    direct_incomes: DirectIncomes
    invoices: Invoices
    credit_notes: CreditNotes
    payments: Payments
    reports: Reports

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.customers = Customers(self.sdk_configuration)
        self.direct_incomes = DirectIncomes(self.sdk_configuration)
        self.invoices = Invoices(self.sdk_configuration)
        self.credit_notes = CreditNotes(self.sdk_configuration)
        self.payments = Payments(self.sdk_configuration)
        self.reports = Reports(self.sdk_configuration)