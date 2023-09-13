"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .accounts_payable_bill_credit_notes import AccountsPayableBillCreditNotes
from .accounts_payable_bill_payments import AccountsPayableBillPayments
from .accounts_payable_bills import AccountsPayableBills
from .accounts_payable_suppliers import AccountsPayableSuppliers
from .sdkconfiguration import SDKConfiguration

class AccountsPayable:
    r"""Data from a linked accounting platform representing money the business owes money to its suppliers."""
    bill_credit_notes: AccountsPayableBillCreditNotes
    bill_payments: AccountsPayableBillPayments
    bills: AccountsPayableBills
    suppliers: AccountsPayableSuppliers
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.bill_credit_notes = AccountsPayableBillCreditNotes(self.sdk_configuration)
        self.bill_payments = AccountsPayableBillPayments(self.sdk_configuration)
        self.bills = AccountsPayableBills(self.sdk_configuration)
        self.suppliers = AccountsPayableSuppliers(self.sdk_configuration)
        
    