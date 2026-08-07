"""codat_lending.models.shared — domain-shared models."""

from importlib import import_module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .security import Security, SecurityTypedDict
    from codat_lending.models.account import Account, AccountTypedDict
    from codat_lending.models.shared.accountbalance import AccountBalance, AccountBalanceTypedDict
    from codat_lending.models.shared.accountbalanceamounts import AccountBalanceAmounts, AccountBalanceAmountsTypedDict
    from codat_lending.models.shared.accountcategoriesupdatedwebhook import AccountCategoriesUpdatedWebhook, AccountCategoriesUpdatedWebhookTypedDict
    from codat_lending.models.shared.accountcategoriesupdatedwebhookdata import AccountCategoriesUpdatedWebhookData, AccountCategoriesUpdatedWebhookDataTypedDict
    from codat_lending.models.shared.accountcategorylevel import AccountCategoryLevel, AccountCategoryLevelTypedDict
    from codat_lending.models.shared.accountidentifiertype import AccountIdentifierType
    from codat_lending.models.shared.accountidentifiers import AccountIdentifiers, AccountIdentifiersTypedDict
    from codat_lending.models.shared.accountinfo import AccountInfo, AccountInfoTypedDict
    from codat_lending.models.shared.accountinstitution import AccountInstitution, AccountInstitutionTypedDict
    from codat_lending.models.shared.accountprototype import AccountPrototype, AccountPrototypeTypedDict
    from codat_lending.models.shared.accountref import AccountRef, AccountRefTypedDict
    from codat_lending.models.shared.accountstatus import AccountStatus
    from codat_lending.models.shared.accounttransactionline import AccountTransactionLine, AccountTransactionLineTypedDict
    from codat_lending.models.account_transaction_line_record_ref import AccountTransactionLineRecordRef, AccountTransactionLineRecordRefTypedDict
    from codat_lending.models.shared.accounttype import AccountType
    from codat_lending.models.shared.accountingaccount import AccountingAccount, AccountingAccountTypedDict
    from codat_lending.models.shared.accountingaccounttransaction import AccountingAccountTransaction, AccountingAccountTransactionTypedDict
    from codat_lending.models.accounting_account_transaction_data_type import AccountingAccountTransactionDataType
    from codat_lending.models.accounting_account_transaction_status import AccountingAccountTransactionStatus
    from codat_lending.models.shared.accountingaccounttransactions import AccountingAccountTransactions, AccountingAccountTransactionsTypedDict
    from codat_lending.models.shared.accountingaccounts import AccountingAccounts, AccountingAccountsTypedDict
    from codat_lending.models.shared.accountingaddress import AccountingAddress, AccountingAddressTypedDict
    from codat_lending.models.shared.accountingaddresstype import AccountingAddressType
    from codat_lending.models.shared.accountingagedcreditorreport import AccountingAgedCreditorReport, AccountingAgedCreditorReportTypedDict
    from codat_lending.models.shared.accountingageddebtorreport import AccountingAgedDebtorReport, AccountingAgedDebtorReportTypedDict
    from codat_lending.models.shared.accountingattachment import AccountingAttachment, AccountingAttachmentTypedDict
    from codat_lending.models.shared.accountingbalancesheet import AccountingBalanceSheet, AccountingBalanceSheetTypedDict
    from codat_lending.models.shared.accountingbankaccount import AccountingBankAccount, AccountingBankAccountTypedDict
    from codat_lending.models.shared.accountingbankaccounttype import AccountingBankAccountType
    from codat_lending.models.shared.accountingbankaccounts import AccountingBankAccounts, AccountingBankAccountsTypedDict
    from codat_lending.models.shared.accountingbanktransaction import AccountingBankTransaction, AccountingBankTransactionTypedDict
    from codat_lending.models.shared.accountingbanktransactions import AccountingBankTransactions, AccountingBankTransactionsTypedDict
    from codat_lending.models.shared.accountingbill import AccountingBill, AccountingBillTypedDict
    from codat_lending.models.shared.accountingbillcreditnote import AccountingBillCreditNote, AccountingBillCreditNoteTypedDict
    from codat_lending.models.shared.accountingbillcreditnotes import AccountingBillCreditNotes, AccountingBillCreditNotesTypedDict
    from codat_lending.models.shared.accountingbillpayment import AccountingBillPayment, AccountingBillPaymentTypedDict
    from codat_lending.models.accounting_bill_payment_all_of_payment_method_ref import AccountingBillPaymentAllOfPaymentMethodRef, AccountingBillPaymentAllOfPaymentMethodRefTypedDict
    from codat_lending.models.accounting_bill_payment_all_of_supplier_ref import AccountingBillPaymentAllOfSupplierRef, AccountingBillPaymentAllOfSupplierRefTypedDict
    from codat_lending.models.shared.accountingbillpayments import AccountingBillPayments, AccountingBillPaymentsTypedDict
    from codat_lending.models.shared.accountingbills import AccountingBills, AccountingBillsTypedDict
    from codat_lending.models.shared.accountingcashflowstatement import AccountingCashFlowStatement, AccountingCashFlowStatementTypedDict
    from codat_lending.models.shared.accountingcompanyinfo import AccountingCompanyInfo, AccountingCompanyInfoTypedDict
    from codat_lending.models.shared.accountingcreateaccountresponse import AccountingCreateAccountResponse, AccountingCreateAccountResponseTypedDict
    from codat_lending.models.accounting_create_account_response_all_of_data import AccountingCreateAccountResponseAllOfData, AccountingCreateAccountResponseAllOfDataTypedDict
    from codat_lending.models.shared.accountingcreatebankaccountresponse import AccountingCreateBankAccountResponse, AccountingCreateBankAccountResponseTypedDict
    from codat_lending.models.accounting_create_bank_account_response_all_of_data import AccountingCreateBankAccountResponseAllOfData, AccountingCreateBankAccountResponseAllOfDataTypedDict
    from codat_lending.models.shared.accountingcreatebanktransactions import AccountingCreateBankTransactions, AccountingCreateBankTransactionsTypedDict
    from codat_lending.models.shared.accountingcreatebanktransactionsresponse import AccountingCreateBankTransactionsResponse, AccountingCreateBankTransactionsResponseTypedDict
    from codat_lending.models.accounting_create_bank_transactions_response_all_of_data import AccountingCreateBankTransactionsResponseAllOfData, AccountingCreateBankTransactionsResponseAllOfDataTypedDict
    from codat_lending.models.shared.accountingcreatedirectcostresponse import AccountingCreateDirectCostResponse, AccountingCreateDirectCostResponseTypedDict
    from codat_lending.models.accounting_create_direct_cost_response_all_of_data import AccountingCreateDirectCostResponseAllOfData, AccountingCreateDirectCostResponseAllOfDataTypedDict
    from codat_lending.models.shared.accountingcreatepaymentresponse import AccountingCreatePaymentResponse, AccountingCreatePaymentResponseTypedDict
    from codat_lending.models.accounting_create_payment_response_all_of_data import AccountingCreatePaymentResponseAllOfData, AccountingCreatePaymentResponseAllOfDataTypedDict
    from codat_lending.models.shared.accountingcreatesupplierresponse import AccountingCreateSupplierResponse, AccountingCreateSupplierResponseTypedDict
    from codat_lending.models.accounting_create_supplier_response_all_of_data import AccountingCreateSupplierResponseAllOfData, AccountingCreateSupplierResponseAllOfDataTypedDict
    from codat_lending.models.accounting_create_transfer_response import AccountingCreateTransferResponse, AccountingCreateTransferResponseTypedDict
    from codat_lending.models.accounting_create_transfer_response_all_of_data import AccountingCreateTransferResponseAllOfData, AccountingCreateTransferResponseAllOfDataTypedDict
    from codat_lending.models.shared.accountingcreditnote import AccountingCreditNote, AccountingCreditNoteTypedDict
    from codat_lending.models.shared.accountingcreditnotes import AccountingCreditNotes, AccountingCreditNotesTypedDict
    from codat_lending.models.shared.accountingcustomer import AccountingCustomer, AccountingCustomerTypedDict
    from codat_lending.models.shared.accountingcustomerref import AccountingCustomerRef, AccountingCustomerRefTypedDict
    from codat_lending.models.shared.accountingcustomers import AccountingCustomers, AccountingCustomersTypedDict
    from codat_lending.models.shared.accountingdirectcost import AccountingDirectCost, AccountingDirectCostTypedDict
    from codat_lending.models.shared.accountingdirectcosts import AccountingDirectCosts, AccountingDirectCostsTypedDict
    from codat_lending.models.shared.accountingdirectincome import AccountingDirectIncome, AccountingDirectIncomeTypedDict
    from codat_lending.models.shared.accountingdirectincomes import AccountingDirectIncomes, AccountingDirectIncomesTypedDict
    from codat_lending.models.shared.accountinginvoice import AccountingInvoice, AccountingInvoiceTypedDict
    from codat_lending.models.accounting_invoice_data_type import AccountingInvoiceDataType
    from codat_lending.models.shared.accountinginvoices import AccountingInvoices, AccountingInvoicesTypedDict
    from codat_lending.models.shared.accountingjournal import AccountingJournal, AccountingJournalTypedDict
    from codat_lending.models.shared.accountingjournalentries import AccountingJournalEntries, AccountingJournalEntriesTypedDict
    from codat_lending.models.shared.accountingjournalentry import AccountingJournalEntry, AccountingJournalEntryTypedDict
    from codat_lending.models.accounting_journal_entry_data_type import AccountingJournalEntryDataType
    from codat_lending.models.shared.accountingjournals import AccountingJournals, AccountingJournalsTypedDict
    from codat_lending.models.shared.accountingpayment import AccountingPayment, AccountingPaymentTypedDict
    from codat_lending.models.shared.accountingpaymentallocation import AccountingPaymentAllocation, AccountingPaymentAllocationTypedDict
    from codat_lending.models.accounting_payment_allocation_allocation import AccountingPaymentAllocationAllocation, AccountingPaymentAllocationAllocationTypedDict
    from codat_lending.models.accounting_payment_method import AccountingPaymentMethod, AccountingPaymentMethodTypedDict
    from codat_lending.models.shared.accountingpayments import AccountingPayments, AccountingPaymentsTypedDict
    from codat_lending.models.shared.accountingprofitandlossreport import AccountingProfitAndLossReport, AccountingProfitAndLossReportTypedDict
    from codat_lending.models.shared.accountingrecordref import AccountingRecordRef, AccountingRecordRefTypedDict
    from codat_lending.models.shared.accountingsupplier import AccountingSupplier, AccountingSupplierTypedDict
    from codat_lending.models.shared.accountingsuppliers import AccountingSuppliers, AccountingSuppliersTypedDict
    from codat_lending.models.accounting_tracking_category import AccountingTrackingCategory, AccountingTrackingCategoryTypedDict
    from codat_lending.models.shared.accountingtransfer import AccountingTransfer, AccountingTransferTypedDict
    from codat_lending.models.accounting_transfer_status import AccountingTransferStatus
    from codat_lending.models.shared.accountingtransfers import AccountingTransfers, AccountingTransfersTypedDict
    from codat_lending.models.shared.accounts import Accounts, AccountsTypedDict
    from codat_lending.models.shared.accountspayabletracking import AccountsPayableTracking, AccountsPayableTrackingTypedDict
    from codat_lending.models.shared.accountsreceivabletracking import AccountsReceivableTracking, AccountsReceivableTrackingTypedDict
    from codat_lending.models.shared.agedcreditor import AgedCreditor, AgedCreditorTypedDict
    from codat_lending.models.shared.agedcurrencyoutstanding import AgedCurrencyOutstanding, AgedCurrencyOutstandingTypedDict
    from codat_lending.models.shared.ageddebtor import AgedDebtor, AgedDebtorTypedDict
    from codat_lending.models.shared.agedoutstandingamount import AgedOutstandingAmount, AgedOutstandingAmountTypedDict
    from codat_lending.models.shared.agedoutstandingamountdetail import AgedOutstandingAmountDetail, AgedOutstandingAmountDetailTypedDict
    from codat_lending.models.shared.attachments import Attachments, AttachmentsTypedDict
    from codat_lending.models.shared.balancesheet import BalanceSheet, BalanceSheetTypedDict
    from codat_lending.models.bank_account_prototype import BankAccountPrototype, BankAccountPrototypeTypedDict
    from codat_lending.models.shared.bankaccountref import BankAccountRef, BankAccountRefTypedDict
    from codat_lending.models.shared.bankaccountstatus import BankAccountStatus
    from codat_lending.models.shared.bankfeedbankaccountmapping import BankFeedBankAccountMapping, BankFeedBankAccountMappingTypedDict
    from codat_lending.models.shared.bankfeedbankaccountmappingresponse import BankFeedBankAccountMappingResponse, BankFeedBankAccountMappingResponseTypedDict
    from codat_lending.models.shared.bankfeedmapping import BankFeedMapping, BankFeedMappingTypedDict
    from codat_lending.models.shared.bankstatementuploadconfiguration import BankStatementUploadConfiguration, BankStatementUploadConfigurationTypedDict
    from codat_lending.models.shared.banktransactiontype import BankTransactionType
    from codat_lending.models.shared.bankingaccount import BankingAccount, BankingAccountTypedDict
    from codat_lending.models.shared.bankingaccountbalance import BankingAccountBalance, BankingAccountBalanceTypedDict
    from codat_lending.models.shared.bankingaccountbalances import BankingAccountBalances, BankingAccountBalancesTypedDict
    from codat_lending.models.shared.bankingaccounts import BankingAccounts, BankingAccountsTypedDict
    from codat_lending.models.shared.bankingtransaction import BankingTransaction, BankingTransactionTypedDict
    from codat_lending.models.shared.bankingtransactioncategories import BankingTransactionCategories, BankingTransactionCategoriesTypedDict
    from codat_lending.models.shared.bankingtransactioncategory import BankingTransactionCategory, BankingTransactionCategoryTypedDict
    from codat_lending.models.shared.bankingtransactionref import BankingTransactionRef, BankingTransactionRefTypedDict
    from codat_lending.models.shared.bankingtransactions import BankingTransactions, BankingTransactionsTypedDict
    from codat_lending.models.shared.billcreditnotelineitem import BillCreditNoteLineItem, BillCreditNoteLineItemTypedDict
    from codat_lending.models.shared.billcreditnotestatus import BillCreditNoteStatus
    from codat_lending.models.bill_line_item import BillLineItem, BillLineItemTypedDict
    from codat_lending.models.bill_line_item_purchase_order_line_ref import BillLineItemPurchaseOrderLineRef, BillLineItemPurchaseOrderLineRefTypedDict
    from codat_lending.models.bill_line_item_purchase_order_line_ref_data_type import BillLineItemPurchaseOrderLineRefDataType
    from codat_lending.models.shared.billpaymentline import BillPaymentLine, BillPaymentLineTypedDict
    from codat_lending.models.shared.billpaymentlinelink import BillPaymentLineLink, BillPaymentLineLinkTypedDict
    from codat_lending.models.shared.billpaymentlinelinktype import BillPaymentLineLinkType
    from codat_lending.models.shared.billstatus import BillStatus
    from codat_lending.models.shared.billedtotype import BilledToType
    from codat_lending.models.shared.billedtotype1 import BilledToType1
    from codat_lending.models.shared.cashflowstatement import CashFlowStatement, CashFlowStatementTypedDict
    from codat_lending.models.cash_flow_transaction import CashFlowTransaction, CashFlowTransactionTypedDict
    from codat_lending.models.categorized_bank_statement_accounts import CategorizedBankStatementAccounts, CategorizedBankStatementAccountsTypedDict
    from codat_lending.models.categorized_bank_statement_transactions import CategorizedBankStatementTransactions, CategorizedBankStatementTransactionsTypedDict
    from codat_lending.models.shared.clientratelimitwebhook import ClientRateLimitWebhook, ClientRateLimitWebhookTypedDict
    from codat_lending.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayload, ClientRateLimitWebhookPayloadTypedDict
    from codat_lending.models.shared.commerceaddress import CommerceAddress, CommerceAddressTypedDict
    from codat_lending.models.shared.commerceaddresstype import CommerceAddressType
    from codat_lending.models.shared.commercecompanyinfo import CommerceCompanyInfo, CommerceCompanyInfoTypedDict
    from codat_lending.models.shared.commercecustomer import CommerceCustomer, CommerceCustomerTypedDict
    from codat_lending.models.shared.commercecustomerref import CommerceCustomerRef, CommerceCustomerRefTypedDict
    from codat_lending.models.shared.commercecustomers import CommerceCustomers, CommerceCustomersTypedDict
    from codat_lending.models.shared.commercedispute import CommerceDispute, CommerceDisputeTypedDict
    from codat_lending.models.shared.commercedisputes import CommerceDisputes, CommerceDisputesTypedDict
    from codat_lending.models.shared.commercelocation import CommerceLocation, CommerceLocationTypedDict
    from codat_lending.models.shared.commercelocations import CommerceLocations, CommerceLocationsTypedDict
    from codat_lending.models.shared.commerceorder import CommerceOrder, CommerceOrderTypedDict
    from codat_lending.models.shared.commerceorders import CommerceOrders, CommerceOrdersTypedDict
    from codat_lending.models.shared.commercepayment import CommercePayment, CommercePaymentTypedDict
    from codat_lending.models.shared.commercepaymentmethod import CommercePaymentMethod, CommercePaymentMethodTypedDict
    from codat_lending.models.commerce_payment_method_status import CommercePaymentMethodStatus
    from codat_lending.models.shared.commercepaymentmethods import CommercePaymentMethods, CommercePaymentMethodsTypedDict
    from codat_lending.models.shared.commercepayments import CommercePayments, CommercePaymentsTypedDict
    from codat_lending.models.shared.commerceproduct import CommerceProduct, CommerceProductTypedDict
    from codat_lending.models.shared.commerceproductcategories import CommerceProductCategories, CommerceProductCategoriesTypedDict
    from codat_lending.models.shared.commerceproductcategory import CommerceProductCategory, CommerceProductCategoryTypedDict
    from codat_lending.models.shared.commerceproducts import CommerceProducts, CommerceProductsTypedDict
    from codat_lending.models.shared.commercerecordref import CommerceRecordRef, CommerceRecordRefTypedDict
    from codat_lending.models.shared.commercereport import CommerceReport, CommerceReportTypedDict
    from codat_lending.models.shared.commercereportcomponent import CommerceReportComponent, CommerceReportComponentTypedDict
    from codat_lending.models.shared.commercereportdimension import CommerceReportDimension, CommerceReportDimensionTypedDict
    from codat_lending.models.commerce_report_dimension_items import CommerceReportDimensionItems, CommerceReportDimensionItemsTypedDict
    from codat_lending.models.shared.commercereporterror import CommerceReportError, CommerceReportErrorTypedDict
    from codat_lending.models.shared.commercereportmeasure import CommerceReportMeasure, CommerceReportMeasureTypedDict
    from codat_lending.models.commerce_tax_component import CommerceTaxComponent, CommerceTaxComponentTypedDict
    from codat_lending.models.shared.commercetransaction import CommerceTransaction, CommerceTransactionTypedDict
    from codat_lending.models.shared.commercetransactions import CommerceTransactions, CommerceTransactionsTypedDict
    from codat_lending.models.shared.companies import Companies, CompaniesTypedDict
    from codat_lending.models.shared.company import Company, CompanyTypedDict
    from codat_lending.models.company_details import CompanyDetails, CompanyDetailsTypedDict
    from codat_lending.models.shared.companyreference import CompanyReference, CompanyReferenceTypedDict
    from codat_lending.models.company_reference_links import CompanyReferenceLinks, CompanyReferenceLinksTypedDict
    from codat_lending.models.shared.companyrequestbody import CompanyRequestBody, CompanyRequestBodyTypedDict
    from codat_lending.models.shared.companyupdaterequest import CompanyUpdateRequest, CompanyUpdateRequestTypedDict
    from codat_lending.models.shared.connection import Connection, ConnectionTypedDict
    from codat_lending.models.shared.connections import Connections, ConnectionsTypedDict
    from codat_lending.models.shared.contact import Contact, ContactTypedDict
    from codat_lending.models.contact_ref import ContactRef, ContactRefTypedDict
    from codat_lending.models.contact_reference import ContactReference, ContactReferenceTypedDict
    from codat_lending.models.shared.createbankaccounttransaction import CreateBankAccountTransaction, CreateBankAccountTransactionTypedDict
    from codat_lending.models.create_connection_request import CreateConnectionRequest, CreateConnectionRequestTypedDict
    from codat_lending.models.create_source_account200_response import CreateSourceAccount200Response, CreateSourceAccount200ResponseTypedDict
    from codat_lending.models.create_source_account_request import CreateSourceAccountRequest, CreateSourceAccountRequestTypedDict
    from codat_lending.models.created_date import CreatedDate, CreatedDateTypedDict
    from codat_lending.models.shared.creditnotelineitem import CreditNoteLineItem, CreditNoteLineItemTypedDict
    from codat_lending.models.shared.creditnotestatus import CreditNoteStatus
    from codat_lending.models.current_status import CurrentStatus
    from codat_lending.models.shared.customerstatus import CustomerStatus
    from codat_lending.models.shared.dataconnectionerror import DataConnectionError, DataConnectionErrorTypedDict
    from codat_lending.models.shared.dataconnectionstatus import DataConnectionStatus
    from codat_lending.models.shared.dataintegrityamounts import DataIntegrityAmounts, DataIntegrityAmountsTypedDict
    from codat_lending.models.shared.dataintegritybyamount import DataIntegrityByAmount, DataIntegrityByAmountTypedDict
    from codat_lending.models.shared.dataintegritybycount import DataIntegrityByCount, DataIntegrityByCountTypedDict
    from codat_lending.models.shared.dataintegrityconnectionid import DataIntegrityConnectionId, DataIntegrityConnectionIdTypedDict
    from codat_lending.models.shared.dataintegritydates import DataIntegrityDates, DataIntegrityDatesTypedDict
    from codat_lending.models.shared.dataintegritydetail import DataIntegrityDetail, DataIntegrityDetailTypedDict
    from codat_lending.models.shared.dataintegritydetails import DataIntegrityDetails, DataIntegrityDetailsTypedDict
    from codat_lending.models.shared.dataintegritymatch import DataIntegrityMatch, DataIntegrityMatchTypedDict
    from codat_lending.models.shared.dataintegritystatus import DataIntegrityStatus, DataIntegrityStatusTypedDict
    from codat_lending.models.shared.dataintegritystatusinfo import DataIntegrityStatusInfo, DataIntegrityStatusInfoTypedDict
    from codat_lending.models.shared.dataintegritystatuses import DataIntegrityStatuses, DataIntegrityStatusesTypedDict
    from codat_lending.models.shared.dataintegritysummaries import DataIntegritySummaries, DataIntegritySummariesTypedDict
    from codat_lending.models.shared.dataintegritysummary import DataIntegritySummary, DataIntegritySummaryTypedDict
    from codat_lending.models.data_integrity_type import DataIntegrityType, DataIntegrityTypeTypedDict
    from codat_lending.models.shared.datasource import DataSource, DataSourceTypedDict
    from codat_lending.models.shared.datastatus import DataStatus, DataStatusTypedDict
    from codat_lending.models.data_statuses import DataStatuses, DataStatusesTypedDict
    from codat_lending.models.shared.datatype import DataType
    from codat_lending.models.data_types import DataTypes
    from codat_lending.models.dataset_status import DatasetStatus
    from codat_lending.models.shared.directcostlineitem import DirectCostLineItem, DirectCostLineItemTypedDict
    from codat_lending.models.shared.directcostprototype import DirectCostPrototype, DirectCostPrototypeTypedDict
    from codat_lending.models.shared.directincomelineitem import DirectIncomeLineItem, DirectIncomeLineItemTypedDict
    from codat_lending.models.shared.disputestatus import DisputeStatus
    from codat_lending.models.shared.enduploadsessionrequest import EndUploadSessionRequest, EndUploadSessionRequestTypedDict
    from codat_lending.models.end_upload_session_request_status import EndUploadSessionRequestStatus
    from codat_lending.models.shared.enhancedcashflowitem import EnhancedCashFlowItem, EnhancedCashFlowItemTypedDict
    from codat_lending.models.shared.enhancedcashflowtransactions import EnhancedCashFlowTransactions, EnhancedCashFlowTransactionsTypedDict
    from codat_lending.models.shared.enhancedfinancialreport import EnhancedFinancialReport, EnhancedFinancialReportTypedDict
    from codat_lending.models.shared.enhancedinvoicereportitem import EnhancedInvoiceReportItem, EnhancedInvoiceReportItemTypedDict
    from codat_lending.models.shared.enhancedinvoicesreport import EnhancedInvoicesReport, EnhancedInvoicesReportTypedDict
    from codat_lending.models.shared.enhancedreportaccountcategory import EnhancedReportAccountCategory, EnhancedReportAccountCategoryTypedDict
    from codat_lending.models.shared.enhancedreportinfo import EnhancedReportInfo, EnhancedReportInfoTypedDict
    from codat_lending.models.error_message import ErrorMessage, ErrorMessageTypedDict
    from codat_lending.models.error_status import ErrorStatus
    from codat_lending.models.shared.errorvalidation import ErrorValidation, ErrorValidationTypedDict
    from codat_lending.models.shared.errorvalidationitem import ErrorValidationItem, ErrorValidationItemTypedDict
    from codat_lending.models.shared.excelreporttypes import ExcelReportTypes
    from codat_lending.models.shared.excelstatus import ExcelStatus, ExcelStatusTypedDict
    from codat_lending.models.shared.file import File, FileTypedDict
    from codat_lending.models.financial_summary import FinancialSummary, FinancialSummaryTypedDict
    from codat_lending.models.financial_summary_accounting_score import FinancialSummaryAccountingScore, FinancialSummaryAccountingScoreTypedDict
    from codat_lending.models.financial_summary_books_closed_date import FinancialSummaryBooksClosedDate, FinancialSummaryBooksClosedDateTypedDict
    from codat_lending.models.get_report_status_report_id_parameter import GetReportStatusReportIdParameter, GetReportStatusReportIdParameterTypedDict
    from codat_lending.models.shared.halref import HalRef, HalRefTypedDict
    from codat_lending.models.shared.integritystatus import IntegrityStatus
    from codat_lending.models.shared.invoicelineitem import InvoiceLineItem, InvoiceLineItemTypedDict
    from codat_lending.models.shared.invoicestatus import InvoiceStatus
    from codat_lending.models.shared.itemref import ItemRef, ItemRefTypedDict
    from codat_lending.models.item_reference import ItemReference, ItemReferenceTypedDict
    from codat_lending.models.shared.items import Items, ItemsTypedDict
    from codat_lending.models.shared.journalentryrecordref import JournalEntryRecordRef, JournalEntryRecordRefTypedDict
    from codat_lending.models.journal_entry_record_ref_data_type import JournalEntryRecordRefDataType
    from codat_lending.models.journal_line import JournalLine, JournalLineTypedDict
    from codat_lending.models.journal_line_tracking import JournalLineTracking, JournalLineTrackingTypedDict
    from codat_lending.models.journal_line_tracking_data_type import JournalLineTrackingDataType
    from codat_lending.models.journal_prototype import JournalPrototype, JournalPrototypeTypedDict
    from codat_lending.models.shared.journalref import JournalRef, JournalRefTypedDict
    from codat_lending.models.shared.journalstatus import JournalStatus
    from codat_lending.models.shared.lendingcustomerref import LendingCustomerRef, LendingCustomerRefTypedDict
    from codat_lending.models.shared.links import Links, LinksTypedDict
    from codat_lending.models.shared.loanref import LoanRef, LoanRefTypedDict
    from codat_lending.models.shared.loansummary import LoanSummary, LoanSummaryTypedDict
    from codat_lending.models.shared.loansummaryintegrationtype import LoanSummaryIntegrationType
    from codat_lending.models.shared.loansummaryrecordref import LoanSummaryRecordRef, LoanSummaryRecordRefTypedDict
    from codat_lending.models.shared.loansummaryrecordreftype import LoanSummaryRecordRefType
    from codat_lending.models.shared.loansummaryreportinfo import LoanSummaryReportInfo, LoanSummaryReportInfoTypedDict
    from codat_lending.models.shared.loansummaryreportitem import LoanSummaryReportItem, LoanSummaryReportItemTypedDict
    from codat_lending.models.loan_transaction_type import LoanTransactionType
    from codat_lending.models.shared.loantransactions import LoanTransactions, LoanTransactionsTypedDict
    from codat_lending.models.shared.loantransactionsreportinfo import LoanTransactionsReportInfo, LoanTransactionsReportInfoTypedDict
    from codat_lending.models.shared.locationref import LocationRef, LocationRefTypedDict
    from codat_lending.models.shared.metadata import Metadata, MetadataTypedDict
    from codat_lending.models.model0 import Model0, Model0TypedDict
    from codat_lending.models.model3 import Model3, Model3TypedDict
    from codat_lending.models.shared.orderdiscountallocation import OrderDiscountAllocation, OrderDiscountAllocationTypedDict
    from codat_lending.models.shared.orderlineitem import OrderLineItem, OrderLineItemTypedDict
    from codat_lending.models.paging_info import PagingInfo, PagingInfoTypedDict
    from codat_lending.models.shared.payment import Payment, PaymentTypedDict
    from codat_lending.models.shared.paymentallocationpayment import PaymentAllocationPayment, PaymentAllocationPaymentTypedDict
    from codat_lending.models.shared.paymentline import PaymentLine, PaymentLineTypedDict
    from codat_lending.models.shared.paymentlinelink import PaymentLineLink, PaymentLineLinkTypedDict
    from codat_lending.models.shared.paymentlinktype import PaymentLinkType
    from codat_lending.models.shared.paymentmethodref import PaymentMethodRef, PaymentMethodRefTypedDict
    from codat_lending.models.payment_method_type import PaymentMethodType
    from codat_lending.models.shared.paymentref import PaymentRef, PaymentRefTypedDict
    from codat_lending.models.shared.paymentstatus import PaymentStatus
    from codat_lending.models.shared.paymenttype import PaymentType
    from codat_lending.models.phone_number import PhoneNumber, PhoneNumberTypedDict
    from codat_lending.models.shared.productinventory import ProductInventory, ProductInventoryTypedDict
    from codat_lending.models.shared.productinventorylocation import ProductInventoryLocation, ProductInventoryLocationTypedDict
    from codat_lending.models.shared.productprice import ProductPrice, ProductPriceTypedDict
    from codat_lending.models.shared.productref import ProductRef, ProductRefTypedDict
    from codat_lending.models.shared.productvariant import ProductVariant, ProductVariantTypedDict
    from codat_lending.models.shared.productvariantref import ProductVariantRef, ProductVariantRefTypedDict
    from codat_lending.models.shared.productvariantstatus import ProductVariantStatus
    from codat_lending.models.shared.profitandlossreport import ProfitAndLossReport, ProfitAndLossReportTypedDict
    from codat_lending.models.shared.projectref import ProjectRef, ProjectRefTypedDict
    from codat_lending.models.shared.pulloperation import PullOperation, PullOperationTypedDict
    from codat_lending.models.shared.pulloperations import PullOperations, PullOperationsTypedDict
    from codat_lending.models.purchase_order_reference import PurchaseOrderReference, PurchaseOrderReferenceTypedDict
    from codat_lending.models.shared.pushchangetype import PushChangeType
    from codat_lending.models.shared.pushfieldvalidation import PushFieldValidation, PushFieldValidationTypedDict
    from codat_lending.models.shared.pushoperation import PushOperation, PushOperationTypedDict
    from codat_lending.models.shared.pushoperationchange import PushOperationChange, PushOperationChangeTypedDict
    from codat_lending.models.shared.pushoperationref import PushOperationRef, PushOperationRefTypedDict
    from codat_lending.models.shared.pushoperationstatus import PushOperationStatus
    from codat_lending.models.shared.pushoperations import PushOperations, PushOperationsTypedDict
    from codat_lending.models.shared.pushoption import PushOption, PushOptionTypedDict
    from codat_lending.models.shared.pushoptionchoice import PushOptionChoice, PushOptionChoiceTypedDict
    from codat_lending.models.shared.pushoptionproperty import PushOptionProperty, PushOptionPropertyTypedDict
    from codat_lending.models.shared.pushoptiontype import PushOptionType
    from codat_lending.models.shared.pushvalidationinfo import PushValidationInfo, PushValidationInfoTypedDict
    from codat_lending.models.record_line_reference import RecordLineReference, RecordLineReferenceTypedDict
    from codat_lending.models.record_line_reference_data_type import RecordLineReferenceDataType
    from codat_lending.models.shared.reportbasis import ReportBasis
    from codat_lending.models.shared.reportcomponentmeasure import ReportComponentMeasure, ReportComponentMeasureTypedDict
    from codat_lending.models.shared.reportinfo import ReportInfo, ReportInfoTypedDict
    from codat_lending.models.shared.reportinput import ReportInput
    from codat_lending.models.report_item import ReportItem, ReportItemTypedDict
    from codat_lending.models.shared.reportitems import ReportItems, ReportItemsTypedDict
    from codat_lending.models.shared.reportline import ReportLine, ReportLineTypedDict
    from codat_lending.models.shared.reportoperation import ReportOperation, ReportOperationTypedDict
    from codat_lending.models.report_operation_status import ReportOperationStatus
    from codat_lending.models.report_operation_type import ReportOperationType
    from codat_lending.models.report_source_reference import ReportSourceReference, ReportSourceReferenceTypedDict
    from codat_lending.models.shared.reports import Reports, ReportsTypedDict
    from codat_lending.models.shared.routinginfo import RoutingInfo, RoutingInfoTypedDict
    from codat_lending.models.sales_order_reference import SalesOrderReference, SalesOrderReferenceTypedDict
    from codat_lending.models.shared.servicecharge import ServiceCharge, ServiceChargeTypedDict
    from codat_lending.models.shared.servicechargetype import ServiceChargeType
    from codat_lending.models.source import Source
    from codat_lending.models.shared.sourceaccount import SourceAccount, SourceAccountTypedDict
    from codat_lending.models.shared.sourceaccountprototype import SourceAccountPrototype, SourceAccountPrototypeTypedDict
    from codat_lending.models.source_account_status import SourceAccountStatus
    from codat_lending.models.source_account_v2 import SourceAccountV2, SourceAccountV2TypedDict
    from codat_lending.models.shared.sourceaccountv2prototype import SourceAccountV2Prototype, SourceAccountV2PrototypeTypedDict
    from codat_lending.models.source_account_v2_status import SourceAccountV2Status
    from codat_lending.models.source_account_v2_type import SourceAccountV2Type
    from codat_lending.models.shared.sourceref import SourceRef, SourceRefTypedDict
    from codat_lending.models.source_type import SourceType
    from codat_lending.models.shared.startuploadsessionrequest import StartUploadSessionRequest, StartUploadSessionRequestTypedDict
    from codat_lending.models.start_upload_session_request_data_type import StartUploadSessionRequestDataType
    from codat_lending.models.shared.status import Status
    from codat_lending.models.shared.supplementaldata import SupplementalData, SupplementalDataTypedDict
    from codat_lending.models.shared.supplierref import SupplierRef, SupplierRefTypedDict
    from codat_lending.models.shared.supplierstatus import SupplierStatus
    from codat_lending.models.shared.targetaccountoption import TargetAccountOption, TargetAccountOptionTypedDict
    from codat_lending.models.shared.taxcomponentallocation import TaxComponentAllocation, TaxComponentAllocationTypedDict
    from codat_lending.models.shared.taxcomponentref import TaxComponentRef, TaxComponentRefTypedDict
    from codat_lending.models.shared.taxrateref import TaxRateRef, TaxRateRefTypedDict
    from codat_lending.models.tax_rate_reference import TaxRateReference, TaxRateReferenceTypedDict
    from codat_lending.models.shared.tracking import Tracking, TrackingTypedDict
    from codat_lending.models.shared.trackingcategoryref import TrackingCategoryRef, TrackingCategoryRefTypedDict
    from codat_lending.models.tracking_record_ref import TrackingRecordRef, TrackingRecordRefTypedDict
    from codat_lending.models.shared.transactioncategory import TransactionCategory, TransactionCategoryTypedDict
    from codat_lending.models.shared.transactioncategoryref import TransactionCategoryRef, TransactionCategoryRefTypedDict
    from codat_lending.models.shared.transactioncategorystatus import TransactionCategoryStatus
    from codat_lending.models.shared.transactioncode import TransactionCode
    from codat_lending.models.shared.transactionsourceref import TransactionSourceRef, TransactionSourceRefTypedDict
    from codat_lending.models.shared.transactionsourcetype import TransactionSourceType
    from codat_lending.models.shared.transactiontype import TransactionType
    from codat_lending.models.shared.transferaccount import TransferAccount, TransferAccountTypedDict
    from codat_lending.models.type import Type
    from codat_lending.models.update_connection import UpdateConnection, UpdateConnectionTypedDict
    from codat_lending.models.upload_bank_statement_data_request import UploadBankStatementDataRequest, UploadBankStatementDataRequestTypedDict
    from codat_lending.models.valid_data_type_links import ValidDataTypeLinks, ValidDataTypeLinksTypedDict
    from codat_lending.models.shared.validation import Validation, ValidationTypedDict
    from codat_lending.models.shared.validationitem import ValidationItem, ValidationItemTypedDict
    from codat_lending.models.shared.weblink import WebLink, WebLinkTypedDict
    from codat_lending.models.web_link_type import WebLinkType
    from codat_lending.models.withholding_tax import WithholdingTax, WithholdingTaxTypedDict
    from codat_lending.models.shared.accountingcreatetransferresponse import AccountingCreateTransferResponseStatus
    from codat_lending.models.shared.accounttransactionlinerecordref import AccountTransactionLineRecordRefDataType
    from codat_lending.models.shared.billlineitem import BillLineItemDataType
    from codat_lending.models.shared.contactref import ContactRefDataType
    from codat_lending.models.shared.journalline import JournalLineDataType
    from codat_lending.models.shared.propertie_accounttype import PropertieAccountType
    from codat_lending.models.shared.schema_datatype import SchemaDataType
    from codat_lending.models.shared.sourceaccountv2 import SourceAccountV2AccountType
    from codat_lending.models.shared.trackingrecordref import TrackingRecordRefDataType
    from codat_lending.models.shared.zero import ZeroDataType
    from codat_lending.models.shared.accountbalanceamounts import AccountBalanceAmountsTypedDict as AccountBalanceAmountsTypedDict
    from codat_lending.models.shared.accountbalance import AccountBalanceTypedDict as AccountBalanceTypedDict
    from codat_lending.models.shared.accountcategoriesupdatedwebhookdata import AccountCategoriesUpdatedWebhookDataTypedDict as AccountCategoriesUpdatedWebhookDataTypedDict
    from codat_lending.models.shared.accountcategoriesupdatedwebhook import AccountCategoriesUpdatedWebhookTypedDict as AccountCategoriesUpdatedWebhookTypedDict
    from codat_lending.models.shared.accountcategorylevel import AccountCategoryLevelTypedDict as AccountCategoryLevelTypedDict
    from codat_lending.models.shared.accountidentifiertype import AccountIdentifierType as AccountIdentifierType
    from codat_lending.models.shared.accountidentifiers import AccountIdentifiersTypedDict as AccountIdentifiersTypedDict
    from codat_lending.models.shared.accountinfo import AccountInfoTypedDict as AccountInfoTypedDict
    from codat_lending.models.shared.accountinstitution import AccountInstitutionTypedDict as AccountInstitutionTypedDict
    from codat_lending.models.shared.accountprototype import AccountPrototypeTypedDict as AccountPrototypeTypedDict
    from codat_lending.models.shared.accountref import AccountRefTypedDict as AccountRefTypedDict
    from codat_lending.models.shared.accountstatus import AccountStatus as AccountStatus
    from codat_lending.models.shared.accounttransactionlinerecordref import AccountTransactionLineRecordRefDataType as AccountTransactionLineRecordRefDataType
    from codat_lending.models.account_transaction_line_record_ref import AccountTransactionLineRecordRefTypedDict as AccountTransactionLineRecordRefTypedDict
    from codat_lending.models.shared.accounttransactionline import AccountTransactionLineTypedDict as AccountTransactionLineTypedDict
    from codat_lending.models.shared.accounttype import AccountType as AccountType
    from codat_lending.models.accounting_account_transaction_status import AccountingAccountTransactionStatus as AccountingAccountTransactionStatus
    from codat_lending.models.shared.accountingaccounttransaction import AccountingAccountTransactionTypedDict as AccountingAccountTransactionTypedDict
    from codat_lending.models.shared.accountingaccounttransactions import AccountingAccountTransactionsTypedDict as AccountingAccountTransactionsTypedDict
    from codat_lending.models.shared.accountingaccount import AccountingAccountTypedDict as AccountingAccountTypedDict
    from codat_lending.models.valid_data_type_links import ValidDataTypeLinks as AccountingAccountValidDataTypeLinks
    from codat_lending.models.valid_data_type_links import ValidDataTypeLinksTypedDict as AccountingAccountValidDataTypeLinksTypedDict
    from codat_lending.models.shared.accountingaccounts import AccountingAccountsTypedDict as AccountingAccountsTypedDict
    from codat_lending.models.shared.accountingaddresstype import AccountingAddressType as AccountingAddressType
    from codat_lending.models.shared.accountingaddress import AccountingAddressTypedDict as AccountingAddressTypedDict
    from codat_lending.models.shared.accountingagedcreditorreport import AccountingAgedCreditorReportTypedDict as AccountingAgedCreditorReportTypedDict
    from codat_lending.models.shared.accountingageddebtorreport import AccountingAgedDebtorReportTypedDict as AccountingAgedDebtorReportTypedDict
    from codat_lending.models.shared.accountingattachment import AccountingAttachmentTypedDict as AccountingAttachmentTypedDict
    from codat_lending.models.shared.accountingbalancesheet import AccountingBalanceSheetTypedDict as AccountingBalanceSheetTypedDict
    from codat_lending.models.shared.accountingbankaccounttype import AccountingBankAccountType as AccountingBankAccountType
    from codat_lending.models.shared.accountingbankaccount import AccountingBankAccountTypedDict as AccountingBankAccountTypedDict
    from codat_lending.models.shared.accountingbankaccounts import AccountingBankAccountsTypedDict as AccountingBankAccountsTypedDict
    from codat_lending.models.shared.accountingbanktransaction import AccountingBankTransactionTypedDict as AccountingBankTransactionTypedDict
    from codat_lending.models.shared.accountingbanktransactions import AccountingBankTransactionsTypedDict as AccountingBankTransactionsTypedDict
    from codat_lending.models.shared.accountingbillcreditnote import AccountingBillCreditNoteTypedDict as AccountingBillCreditNoteTypedDict
    from codat_lending.models.shared.accountingbillcreditnotes import AccountingBillCreditNotesTypedDict as AccountingBillCreditNotesTypedDict
    from codat_lending.models.shared.accountingbillpayment import AccountingBillPaymentTypedDict as AccountingBillPaymentTypedDict
    from codat_lending.models.shared.accountingbillpayments import AccountingBillPaymentsTypedDict as AccountingBillPaymentsTypedDict
    from codat_lending.models.shared.accountingbill import AccountingBillTypedDict as AccountingBillTypedDict
    from codat_lending.models.shared.accountingbills import AccountingBillsTypedDict as AccountingBillsTypedDict
    from codat_lending.models.shared.accountingcashflowstatement import AccountingCashFlowStatementTypedDict as AccountingCashFlowStatementTypedDict
    from codat_lending.models.shared.accountingcompanyinfo import AccountingCompanyInfoTypedDict as AccountingCompanyInfoTypedDict
    from codat_lending.models.accounting_create_account_response_all_of_data import AccountingCreateAccountResponseAllOfData as AccountingCreateAccountResponseAccountingAccount
    from codat_lending.models.accounting_create_account_response_all_of_data import AccountingCreateAccountResponseAllOfData as AccountingCreateAccountResponseAccountingAccountTypedDict
    from codat_lending.models.shared.accountingcreateaccountresponse import AccountingCreateAccountResponseTypedDict as AccountingCreateAccountResponseTypedDict
    from codat_lending.models.valid_data_type_links import ValidDataTypeLinks as AccountingCreateAccountResponseValidDataTypeLinks
    from codat_lending.models.valid_data_type_links import ValidDataTypeLinksTypedDict as AccountingCreateAccountResponseValidDataTypeLinksTypedDict
    from codat_lending.models.accounting_create_bank_account_response_all_of_data import AccountingCreateBankAccountResponseAllOfData as AccountingCreateBankAccountResponseAccountingBankAccount
    from codat_lending.models.accounting_create_bank_account_response_all_of_data import AccountingCreateBankAccountResponseAllOfData as AccountingCreateBankAccountResponseAccountingBankAccountTypedDict
    from codat_lending.models.shared.accountingcreatebankaccountresponse import AccountingCreateBankAccountResponseTypedDict as AccountingCreateBankAccountResponseTypedDict
    from codat_lending.models.shared.accountingcreatebanktransactionsresponse import AccountingCreateBankTransactionsResponseTypedDict as AccountingCreateBankTransactionsResponseTypedDict
    from codat_lending.models.shared.accountingcreatebanktransactions import AccountingCreateBankTransactionsTypedDict as AccountingCreateBankTransactionsTypedDict
    from codat_lending.models.accounting_create_direct_cost_response_all_of_data import AccountingCreateDirectCostResponseAllOfData as AccountingCreateDirectCostResponseAccountingDirectCost
    from codat_lending.models.accounting_create_direct_cost_response_all_of_data import AccountingCreateDirectCostResponseAllOfData as AccountingCreateDirectCostResponseAccountingDirectCostTypedDict
    from codat_lending.models.shared.accountingcreatedirectcostresponse import AccountingCreateDirectCostResponseTypedDict as AccountingCreateDirectCostResponseTypedDict
    from codat_lending.models.accounting_create_payment_response_all_of_data import AccountingCreatePaymentResponseAllOfData as AccountingCreatePaymentResponseAccountingPayment
    from codat_lending.models.accounting_create_payment_response_all_of_data import AccountingCreatePaymentResponseAllOfData as AccountingCreatePaymentResponseAccountingPaymentTypedDict
    from codat_lending.models.shared.accountingcreatepaymentresponse import AccountingCreatePaymentResponseTypedDict as AccountingCreatePaymentResponseTypedDict
    from codat_lending.models.accounting_create_supplier_response_all_of_data import AccountingCreateSupplierResponseAllOfData as AccountingCreateSupplierResponseAccountingSupplier
    from codat_lending.models.accounting_create_supplier_response_all_of_data import AccountingCreateSupplierResponseAllOfData as AccountingCreateSupplierResponseAccountingSupplierTypedDict
    from codat_lending.models.shared.accountingcreatesupplierresponse import AccountingCreateSupplierResponseTypedDict as AccountingCreateSupplierResponseTypedDict
    from codat_lending.models.accounting_create_transfer_response_all_of_data import AccountingCreateTransferResponseAllOfData as AccountingCreateTransferResponseAccountingTransfer
    from codat_lending.models.accounting_create_transfer_response_all_of_data import AccountingCreateTransferResponseAllOfData as AccountingCreateTransferResponseAccountingTransferTypedDict
    from codat_lending.models.shared.accountingcreatetransferresponse import AccountingCreateTransferResponseStatus as AccountingCreateTransferResponseStatus
    from codat_lending.models.accounting_create_transfer_response import AccountingCreateTransferResponseTypedDict as AccountingCreateTransferResponseTypedDict
    from codat_lending.models.shared.accountingcreditnote import AccountingCreditNoteTypedDict as AccountingCreditNoteTypedDict
    from codat_lending.models.shared.accountingcreditnotes import AccountingCreditNotesTypedDict as AccountingCreditNotesTypedDict
    from codat_lending.models.shared.accountingcustomerref import AccountingCustomerRefTypedDict as AccountingCustomerRefTypedDict
    from codat_lending.models.shared.accountingcustomer import AccountingCustomerTypedDict as AccountingCustomerTypedDict
    from codat_lending.models.shared.accountingcustomers import AccountingCustomersTypedDict as AccountingCustomersTypedDict
    from codat_lending.models.shared.accountingdirectcost import AccountingDirectCostTypedDict as AccountingDirectCostTypedDict
    from codat_lending.models.shared.accountingdirectcosts import AccountingDirectCostsTypedDict as AccountingDirectCostsTypedDict
    from codat_lending.models.shared.accountingdirectincome import AccountingDirectIncomeTypedDict as AccountingDirectIncomeTypedDict
    from codat_lending.models.shared.accountingdirectincomes import AccountingDirectIncomesTypedDict as AccountingDirectIncomesTypedDict
    from codat_lending.models.accounting_invoice_data_type import AccountingInvoiceDataType as AccountingInvoiceDataType
    from codat_lending.models.shared.accountinginvoice import AccountingInvoiceTypedDict as AccountingInvoiceTypedDict
    from codat_lending.models.shared.accountinginvoices import AccountingInvoicesTypedDict as AccountingInvoicesTypedDict
    from codat_lending.models.shared.accountingjournalentries import AccountingJournalEntriesTypedDict as AccountingJournalEntriesTypedDict
    from codat_lending.models.shared.accountingjournalentry import AccountingJournalEntryTypedDict as AccountingJournalEntryTypedDict
    from codat_lending.models.shared.accountingjournal import AccountingJournalTypedDict as AccountingJournalTypedDict
    from codat_lending.models.shared.accountingjournals import AccountingJournalsTypedDict as AccountingJournalsTypedDict
    from codat_lending.models.shared.accountingpaymentallocation import AccountingPaymentAllocationTypedDict as AccountingPaymentAllocationTypedDict
    from codat_lending.models.shared.accountingpayment import AccountingPaymentTypedDict as AccountingPaymentTypedDict
    from codat_lending.models.shared.accountingpayments import AccountingPaymentsTypedDict as AccountingPaymentsTypedDict
    from codat_lending.models.shared.accountingprofitandlossreport import AccountingProfitAndLossReportTypedDict as AccountingProfitAndLossReportTypedDict
    from codat_lending.models.shared.accountingrecordref import AccountingRecordRefTypedDict as AccountingRecordRefTypedDict
    from codat_lending.models.shared.accountingsupplier import AccountingSupplierTypedDict as AccountingSupplierTypedDict
    from codat_lending.models.shared.accountingsuppliers import AccountingSuppliersTypedDict as AccountingSuppliersTypedDict
    from codat_lending.models.accounting_transfer_status import AccountingTransferStatus as AccountingTransferStatus
    from codat_lending.models.shared.accountingtransfer import AccountingTransferTypedDict as AccountingTransferTypedDict
    from codat_lending.models.shared.accountingtransfers import AccountingTransfersTypedDict as AccountingTransfersTypedDict
    from codat_lending.models.shared.accountspayabletracking import AccountsPayableTrackingTypedDict as AccountsPayableTrackingTypedDict
    from codat_lending.models.shared.accountsreceivabletracking import AccountsReceivableTrackingTypedDict as AccountsReceivableTrackingTypedDict
    from codat_lending.models.shared.accounts import AccountsTypedDict as AccountsTypedDict
    from codat_lending.models.shared.agedcreditor import AgedCreditorTypedDict as AgedCreditorTypedDict
    from codat_lending.models.shared.agedcurrencyoutstanding import AgedCurrencyOutstandingTypedDict as AgedCurrencyOutstandingTypedDict
    from codat_lending.models.shared.ageddebtor import AgedDebtorTypedDict as AgedDebtorTypedDict
    from codat_lending.models.shared.agedoutstandingamountdetail import AgedOutstandingAmountDetailTypedDict as AgedOutstandingAmountDetailTypedDict
    from codat_lending.models.shared.agedoutstandingamount import AgedOutstandingAmountTypedDict as AgedOutstandingAmountTypedDict
    from codat_lending.models.accounting_payment_allocation_allocation import AccountingPaymentAllocationAllocation as Allocation
    from codat_lending.models.accounting_payment_allocation_allocation import AccountingPaymentAllocationAllocationTypedDict as AllocationTypedDict
    from codat_lending.models.shared.attachments import AttachmentsTypedDict as AttachmentsTypedDict
    from codat_lending.models.shared.balancesheet import BalanceSheetTypedDict as BalanceSheetTypedDict
    from codat_lending.models.shared.bankaccountref import BankAccountRefTypedDict as BankAccountRefTypedDict
    from codat_lending.models.shared.bankaccountstatus import BankAccountStatus as BankAccountStatus
    from codat_lending.models.shared.bankfeedbankaccountmappingresponse import BankFeedBankAccountMappingResponseTypedDict as BankFeedBankAccountMappingResponseTypedDict
    from codat_lending.models.shared.bankfeedbankaccountmapping import BankFeedBankAccountMappingTypedDict as BankFeedBankAccountMappingTypedDict
    from codat_lending.models.shared.bankfeedmapping import BankFeedMappingTypedDict as BankFeedMappingTypedDict
    from codat_lending.models.shared.bankstatementuploadconfiguration import BankStatementUploadConfigurationTypedDict as BankStatementUploadConfigurationTypedDict
    from codat_lending.models.shared.banktransactiontype import BankTransactionType as BankTransactionType
    from codat_lending.models.shared.bankingaccountbalance import BankingAccountBalanceTypedDict as BankingAccountBalanceTypedDict
    from codat_lending.models.shared.bankingaccountbalances import BankingAccountBalancesTypedDict as BankingAccountBalancesTypedDict
    from codat_lending.models.shared.bankingaccount import BankingAccountTypedDict as BankingAccountTypedDict
    from codat_lending.models.shared.bankingaccounts import BankingAccountsTypedDict as BankingAccountsTypedDict
    from codat_lending.models.shared.bankingtransactioncategories import BankingTransactionCategoriesTypedDict as BankingTransactionCategoriesTypedDict
    from codat_lending.models.shared.bankingtransactioncategory import BankingTransactionCategoryTypedDict as BankingTransactionCategoryTypedDict
    from codat_lending.models.shared.bankingtransactionref import BankingTransactionRefTypedDict as BankingTransactionRefTypedDict
    from codat_lending.models.shared.bankingtransaction import BankingTransactionTypedDict as BankingTransactionTypedDict
    from codat_lending.models.shared.bankingtransactions import BankingTransactionsTypedDict as BankingTransactionsTypedDict
    from codat_lending.models.shared.billcreditnotelineitem import BillCreditNoteLineItemTypedDict as BillCreditNoteLineItemTypedDict
    from codat_lending.models.shared.billcreditnotestatus import BillCreditNoteStatus as BillCreditNoteStatus
    from codat_lending.models.shared.billlineitem import BillLineItemDataType as BillLineItemDataType
    from codat_lending.models.bill_line_item import BillLineItemTypedDict as BillLineItemTypedDict
    from codat_lending.models.shared.billpaymentlinelinktype import BillPaymentLineLinkType as BillPaymentLineLinkType
    from codat_lending.models.shared.billpaymentlinelink import BillPaymentLineLinkTypedDict as BillPaymentLineLinkTypedDict
    from codat_lending.models.shared.billpaymentline import BillPaymentLineTypedDict as BillPaymentLineTypedDict
    from codat_lending.models.shared.billstatus import BillStatus as BillStatus
    from codat_lending.models.shared.billedtotype import BilledToType as BilledToType
    from codat_lending.models.shared.billedtotype1 import BilledToType1 as BilledToType1
    from codat_lending.models.shared.cashflowstatement import CashFlowStatementTypedDict as CashFlowStatementTypedDict
    from codat_lending.models.cash_flow_transaction import CashFlowTransactionTypedDict as CashFlowTransactionTypedDict
    from codat_lending.models.shared.clientratelimitwebhookpayload import ClientRateLimitWebhookPayloadTypedDict as ClientRateLimitWebhookPayloadTypedDict
    from codat_lending.models.shared.clientratelimitwebhook import ClientRateLimitWebhookTypedDict as ClientRateLimitWebhookTypedDict
    from codat_lending.models.shared.commerceaddresstype import CommerceAddressType as CommerceAddressType
    from codat_lending.models.shared.commerceaddress import CommerceAddressTypedDict as CommerceAddressTypedDict
    from codat_lending.models.shared.commercecompanyinfo import CommerceCompanyInfoTypedDict as CommerceCompanyInfoTypedDict
    from codat_lending.models.shared.commercecustomerref import CommerceCustomerRefTypedDict as CommerceCustomerRefTypedDict
    from codat_lending.models.shared.commercecustomer import CommerceCustomerTypedDict as CommerceCustomerTypedDict
    from codat_lending.models.shared.commercecustomers import CommerceCustomersTypedDict as CommerceCustomersTypedDict
    from codat_lending.models.shared.commercedispute import CommerceDisputeTypedDict as CommerceDisputeTypedDict
    from codat_lending.models.shared.commercedisputes import CommerceDisputesTypedDict as CommerceDisputesTypedDict
    from codat_lending.models.shared.commercelocation import CommerceLocationTypedDict as CommerceLocationTypedDict
    from codat_lending.models.shared.commercelocations import CommerceLocationsTypedDict as CommerceLocationsTypedDict
    from codat_lending.models.shared.commerceorder import CommerceOrderTypedDict as CommerceOrderTypedDict
    from codat_lending.models.shared.commerceorders import CommerceOrdersTypedDict as CommerceOrdersTypedDict
    from codat_lending.models.commerce_payment_method_status import CommercePaymentMethodStatus as CommercePaymentMethodStatus
    from codat_lending.models.shared.commercepaymentmethod import CommercePaymentMethodTypedDict as CommercePaymentMethodTypedDict
    from codat_lending.models.shared.commercepaymentmethods import CommercePaymentMethodsTypedDict as CommercePaymentMethodsTypedDict
    from codat_lending.models.shared.commercepayment import CommercePaymentTypedDict as CommercePaymentTypedDict
    from codat_lending.models.shared.commercepayments import CommercePaymentsTypedDict as CommercePaymentsTypedDict
    from codat_lending.models.shared.commerceproductcategories import CommerceProductCategoriesTypedDict as CommerceProductCategoriesTypedDict
    from codat_lending.models.shared.commerceproductcategory import CommerceProductCategoryTypedDict as CommerceProductCategoryTypedDict
    from codat_lending.models.shared.commerceproduct import CommerceProductTypedDict as CommerceProductTypedDict
    from codat_lending.models.shared.commerceproducts import CommerceProductsTypedDict as CommerceProductsTypedDict
    from codat_lending.models.shared.commercerecordref import CommerceRecordRefTypedDict as CommerceRecordRefTypedDict
    from codat_lending.models.shared.commercereportcomponent import CommerceReportComponentTypedDict as CommerceReportComponentTypedDict
    from codat_lending.models.commerce_report_dimension_items import CommerceReportDimensionItemsTypedDict as CommerceReportDimensionItemsTypedDict
    from codat_lending.models.shared.commercereportdimension import CommerceReportDimensionTypedDict as CommerceReportDimensionTypedDict
    from codat_lending.models.shared.commercereporterror import CommerceReportErrorTypedDict as CommerceReportErrorTypedDict
    from codat_lending.models.shared.commercereportmeasure import CommerceReportMeasureTypedDict as CommerceReportMeasureTypedDict
    from codat_lending.models.shared.commercereport import CommerceReportTypedDict as CommerceReportTypedDict
    from codat_lending.models.shared.commercetransaction import CommerceTransactionTypedDict as CommerceTransactionTypedDict
    from codat_lending.models.shared.commercetransactions import CommerceTransactionsTypedDict as CommerceTransactionsTypedDict
    from codat_lending.models.shared.companies import CompaniesTypedDict as CompaniesTypedDict
    from codat_lending.models.company_reference_links import CompanyReferenceLinksTypedDict as CompanyReferenceLinksTypedDict
    from codat_lending.models.shared.companyreference import CompanyReferenceTypedDict as CompanyReferenceTypedDict
    from codat_lending.models.shared.companyrequestbody import CompanyRequestBodyTypedDict as CompanyRequestBodyTypedDict
    from codat_lending.models.shared.company import CompanyTypedDict as CompanyTypedDict
    from codat_lending.models.shared.companyupdaterequest import CompanyUpdateRequestTypedDict as CompanyUpdateRequestTypedDict
    from codat_lending.models.shared.connection import ConnectionTypedDict as ConnectionTypedDict
    from codat_lending.models.shared.connections import ConnectionsTypedDict as ConnectionsTypedDict
    from codat_lending.models.shared.contactref import ContactRefDataType as ContactRefDataType
    from codat_lending.models.contact_ref import ContactRefTypedDict as ContactRefTypedDict
    from codat_lending.models.contact_reference import ContactReferenceTypedDict as ContactReferenceTypedDict
    from codat_lending.models.shared.contact import ContactTypedDict as ContactTypedDict
    from codat_lending.models.shared.createbankaccounttransaction import CreateBankAccountTransactionTypedDict as CreateBankAccountTransactionTypedDict
    from codat_lending.models.shared.creditnotelineitem import CreditNoteLineItemTypedDict as CreditNoteLineItemTypedDict
    from codat_lending.models.shared.creditnotestatus import CreditNoteStatus as CreditNoteStatus
    from codat_lending.models.shared.customerstatus import CustomerStatus as CustomerStatus
    from codat_lending.models.shared.dataconnectionerror import DataConnectionErrorTypedDict as DataConnectionErrorTypedDict
    from codat_lending.models.shared.dataconnectionstatus import DataConnectionStatus as DataConnectionStatus
    from codat_lending.models.shared.dataintegrityamounts import DataIntegrityAmountsTypedDict as DataIntegrityAmountsTypedDict
    from codat_lending.models.shared.dataintegritybyamount import DataIntegrityByAmountTypedDict as DataIntegrityByAmountTypedDict
    from codat_lending.models.shared.dataintegritybycount import DataIntegrityByCountTypedDict as DataIntegrityByCountTypedDict
    from codat_lending.models.shared.dataintegrityconnectionid import DataIntegrityConnectionId as DataIntegrityConnectionID
    from codat_lending.models.shared.dataintegrityconnectionid import DataIntegrityConnectionIdTypedDict as DataIntegrityConnectionIDTypedDict
    from codat_lending.models.shared.dataintegritydatatype import DataIntegrityDataType as DataIntegrityDataType
    from codat_lending.models.shared.dataintegritydates import DataIntegrityDatesTypedDict as DataIntegrityDatesTypedDict
    from codat_lending.models.shared.dataintegritydetail import DataIntegrityDetailTypedDict as DataIntegrityDetailTypedDict
    from codat_lending.models.shared.dataintegritydetails import DataIntegrityDetailsTypedDict as DataIntegrityDetailsTypedDict
    from codat_lending.models.shared.dataintegritymatch import DataIntegrityMatchTypedDict as DataIntegrityMatchTypedDict
    from codat_lending.models.shared.dataintegritystatusinfo import DataIntegrityStatusInfoTypedDict as DataIntegrityStatusInfoTypedDict
    from codat_lending.models.shared.dataintegritystatus import DataIntegrityStatusTypedDict as DataIntegrityStatusTypedDict
    from codat_lending.models.shared.dataintegritystatuses import DataIntegrityStatusesTypedDict as DataIntegrityStatusesTypedDict
    from codat_lending.models.shared.dataintegritysummaries import DataIntegritySummariesTypedDict as DataIntegritySummariesTypedDict
    from codat_lending.models.shared.dataintegritysummary import DataIntegritySummaryTypedDict as DataIntegritySummaryTypedDict
    from codat_lending.models.shared.datasource import DataSourceTypedDict as DataSourceTypedDict
    from codat_lending.models.shared.datastatus import DataStatusTypedDict as DataStatusTypedDict
    from codat_lending.models.shared.datatype import DataType as DataType
    from codat_lending.models.data_types import DataTypes as DataTypes
    from codat_lending.models.dataset_status import DatasetStatus as DatasetStatus
    from codat_lending.models.shared.directcostlineitem import DirectCostLineItemTypedDict as DirectCostLineItemTypedDict
    from codat_lending.models.shared.directcostprototype import DirectCostPrototypeTypedDict as DirectCostPrototypeTypedDict
    from codat_lending.models.shared.directincomelineitem import DirectIncomeLineItemTypedDict as DirectIncomeLineItemTypedDict
    from codat_lending.models.shared.disputestatus import DisputeStatus as DisputeStatus
    from codat_lending.models.end_upload_session_request_status import EndUploadSessionRequestStatus as EndUploadSessionRequestStatus
    from codat_lending.models.shared.enduploadsessionrequest import EndUploadSessionRequestTypedDict as EndUploadSessionRequestTypedDict
    from codat_lending.models.shared.enhancedcashflowitem import EnhancedCashFlowItemTypedDict as EnhancedCashFlowItemTypedDict
    from codat_lending.models.shared.enhancedcashflowtransactions import EnhancedCashFlowTransactionsTypedDict as EnhancedCashFlowTransactionsTypedDict
    from codat_lending.models.shared.enhancedfinancialreport import EnhancedFinancialReportTypedDict as EnhancedFinancialReportTypedDict
    from codat_lending.models.shared.enhancedinvoicereportitem import EnhancedInvoiceReportItemTypedDict as EnhancedInvoiceReportItemTypedDict
    from codat_lending.models.shared.enhancedinvoicesreport import EnhancedInvoicesReportTypedDict as EnhancedInvoicesReportTypedDict
    from codat_lending.models.shared.enhancedreportaccountcategory import EnhancedReportAccountCategoryTypedDict as EnhancedReportAccountCategoryTypedDict
    from codat_lending.models.shared.enhancedreportinfo import EnhancedReportInfoTypedDict as EnhancedReportInfoTypedDict
    from codat_lending.models.error_status import ErrorStatus as ErrorStatus
    from codat_lending.models.shared.errorvalidationitem import ErrorValidationItemTypedDict as ErrorValidationItemTypedDict
    from codat_lending.models.shared.errorvalidation import ErrorValidationTypedDict as ErrorValidationTypedDict
    from codat_lending.models.shared.excelreporttypes import ExcelReportTypes as ExcelReportTypes
    from codat_lending.models.shared.excelstatus import ExcelStatusTypedDict as ExcelStatusTypedDict
    from codat_lending.models.shared.file import FileTypedDict as FileTypedDict
    from codat_lending.models.shared.halref import HalRefTypedDict as HalRefTypedDict
    from codat_lending.models.shared.integritystatus import IntegrityStatus as IntegrityStatus
    from codat_lending.models.shared.invoicelineitem import InvoiceLineItemTypedDict as InvoiceLineItemTypedDict
    from codat_lending.models.shared.invoicestatus import InvoiceStatus as InvoiceStatus
    from codat_lending.models.shared.itemref import ItemRefTypedDict as ItemRefTypedDict
    from codat_lending.models.item_reference import ItemReferenceTypedDict as ItemReferenceTypedDict
    from codat_lending.models.shared.items import ItemsTypedDict as ItemsTypedDict
    from codat_lending.models.journal_entry_record_ref_data_type import JournalEntryRecordRefDataType as JournalEntryRecordRefDataType
    from codat_lending.models.shared.journalentryrecordref import JournalEntryRecordRefTypedDict as JournalEntryRecordRefTypedDict
    from codat_lending.models.shared.journalline import JournalLineDataType as JournalLineDataType
    from codat_lending.models.journal_line_tracking import JournalLineTrackingTypedDict as JournalLineTrackingTypedDict
    from codat_lending.models.journal_line import JournalLineTypedDict as JournalLineTypedDict
    from codat_lending.models.shared.journalref import JournalRefTypedDict as JournalRefTypedDict
    from codat_lending.models.shared.journalstatus import JournalStatus as JournalStatus
    from codat_lending.models.shared.lendingcustomerref import LendingCustomerRefTypedDict as LendingCustomerRefTypedDict
    from codat_lending.models.shared.links import LinksTypedDict as LinksTypedDict
    from codat_lending.models.shared.loanref import LoanRefTypedDict as LoanRefTypedDict
    from codat_lending.models.shared.loansummaryintegrationtype import LoanSummaryIntegrationType as LoanSummaryIntegrationType
    from codat_lending.models.shared.loansummaryrecordreftype import LoanSummaryRecordRefType as LoanSummaryRecordRefType
    from codat_lending.models.shared.loansummaryrecordref import LoanSummaryRecordRefTypedDict as LoanSummaryRecordRefTypedDict
    from codat_lending.models.shared.loansummaryreportinfo import LoanSummaryReportInfoTypedDict as LoanSummaryReportInfoTypedDict
    from codat_lending.models.shared.loansummaryreportitem import LoanSummaryReportItemTypedDict as LoanSummaryReportItemTypedDict
    from codat_lending.models.shared.loansummary import LoanSummaryTypedDict as LoanSummaryTypedDict
    from codat_lending.models.loan_transaction_type import LoanTransactionType as LoanTransactionType
    from codat_lending.models.shared.loantransactionsreportinfo import LoanTransactionsReportInfoTypedDict as LoanTransactionsReportInfoTypedDict
    from codat_lending.models.shared.loantransactions import LoanTransactionsTypedDict as LoanTransactionsTypedDict
    from codat_lending.models.shared.locationref import LocationRefTypedDict as LocationRefTypedDict
    from codat_lending.models.shared.metadata import MetadataTypedDict as MetadataTypedDict
    from codat_lending.models.shared.orderdiscountallocation import OrderDiscountAllocationTypedDict as OrderDiscountAllocationTypedDict
    from codat_lending.models.shared.orderlineitem import OrderLineItemTypedDict as OrderLineItemTypedDict
    from codat_lending.models.shared.path import Path as Path
    from codat_lending.models.shared.paymentallocationpayment import PaymentAllocationPaymentTypedDict as PaymentAllocationPaymentTypedDict
    from codat_lending.models.shared.paymentlinelink import PaymentLineLinkTypedDict as PaymentLineLinkTypedDict
    from codat_lending.models.shared.paymentline import PaymentLineTypedDict as PaymentLineTypedDict
    from codat_lending.models.shared.paymentlinktype import PaymentLinkType as PaymentLinkType
    from codat_lending.models.shared.paymentmethodref import PaymentMethodRefTypedDict as PaymentMethodRefTypedDict
    from codat_lending.models.shared.paymentref import PaymentRefTypedDict as PaymentRefTypedDict
    from codat_lending.models.shared.paymentstatus import PaymentStatus as PaymentStatus
    from codat_lending.models.shared.paymenttype import PaymentType as PaymentType
    from codat_lending.models.shared.payment import PaymentTypedDict as PaymentTypedDict
    from codat_lending.models.shared.periodunit import PeriodUnit as PeriodUnit
    from codat_lending.models.shared.phonenumber import PhoneNumberType as PhoneNumberType
    from codat_lending.models.phone_number import PhoneNumberTypedDict as PhoneNumberTypedDict
    from codat_lending.models.shared.productinventorylocation import ProductInventoryLocationTypedDict as ProductInventoryLocationTypedDict
    from codat_lending.models.shared.productinventory import ProductInventoryTypedDict as ProductInventoryTypedDict
    from codat_lending.models.shared.productprice import ProductPriceTypedDict as ProductPriceTypedDict
    from codat_lending.models.shared.productref import ProductRefTypedDict as ProductRefTypedDict
    from codat_lending.models.shared.productvariantref import ProductVariantRefTypedDict as ProductVariantRefTypedDict
    from codat_lending.models.shared.productvariantstatus import ProductVariantStatus as ProductVariantStatus
    from codat_lending.models.shared.productvariant import ProductVariantTypedDict as ProductVariantTypedDict
    from codat_lending.models.shared.profitandlossreport import ProfitAndLossReportTypedDict as ProfitAndLossReportTypedDict
    from codat_lending.models.shared.projectref import ProjectRefTypedDict as ProjectRefTypedDict
    from codat_lending.models.shared.propertie_accounttype import PropertieAccountType as PropertieAccountType
    from codat_lending.models.item_reference import ItemReference as PropertieItemRef
    from codat_lending.models.item_reference import ItemReferenceTypedDict as PropertieItemRefTypedDict
    from codat_lending.models.shared.pulloperation import PullOperationTypedDict as PullOperationTypedDict
    from codat_lending.models.shared.pulloperations import PullOperationsTypedDict as PullOperationsTypedDict
    from codat_lending.models.purchase_order_reference import PurchaseOrderReferenceTypedDict as PurchaseOrderReferenceTypedDict
    from codat_lending.models.shared.pushchangetype import PushChangeType as PushChangeType
    from codat_lending.models.shared.pushfieldvalidation import PushFieldValidationTypedDict as PushFieldValidationTypedDict
    from codat_lending.models.shared.pushoperationchange import PushOperationChangeTypedDict as PushOperationChangeTypedDict
    from codat_lending.models.shared.pushoperationref import PushOperationRefTypedDict as PushOperationRefTypedDict
    from codat_lending.models.shared.pushoperationstatus import PushOperationStatus as PushOperationStatus
    from codat_lending.models.shared.pushoperation import PushOperationTypedDict as PushOperationTypedDict
    from codat_lending.models.shared.pushoperations import PushOperationsTypedDict as PushOperationsTypedDict
    from codat_lending.models.shared.pushoptionchoice import PushOptionChoiceTypedDict as PushOptionChoiceTypedDict
    from codat_lending.models.shared.pushoptionproperty import PushOptionPropertyTypedDict as PushOptionPropertyTypedDict
    from codat_lending.models.shared.pushoptiontype import PushOptionType as PushOptionType
    from codat_lending.models.shared.pushoption import PushOptionTypedDict as PushOptionTypedDict
    from codat_lending.models.shared.pushvalidationinfo import PushValidationInfoTypedDict as PushValidationInfoTypedDict
    from codat_lending.models.record_line_reference import RecordLineReferenceTypedDict as RecordLineReferenceTypedDict
    from codat_lending.models.shared.reportbasis import ReportBasis as ReportBasis
    from codat_lending.models.shared.reportcomponentmeasure import ReportComponentMeasureTypedDict as ReportComponentMeasureTypedDict
    from codat_lending.models.shared.reportinfo import ReportInfoTypedDict as ReportInfoTypedDict
    from codat_lending.models.shared.reportinput import ReportInput as ReportInput
    from codat_lending.models.report_item import ReportItemTypedDict as ReportItemTypedDict
    from codat_lending.models.shared.reportitems import ReportItemsTypedDict as ReportItemsTypedDict
    from codat_lending.models.shared.reportline import ReportLineTypedDict as ReportLineTypedDict
    from codat_lending.models.report_operation_status import ReportOperationStatus as ReportOperationStatus
    from codat_lending.models.report_operation_type import ReportOperationType as ReportOperationType
    from codat_lending.models.shared.reportoperation import ReportOperationTypedDict as ReportOperationTypedDict
    from codat_lending.models.report_source_reference import ReportSourceReferenceTypedDict as ReportSourceReferenceTypedDict
    from codat_lending.models.shared.reporttype import ReportType as ReportType
    from codat_lending.models.shared.reports import ReportsTypedDict as ReportsTypedDict
    from codat_lending.models.shared.routinginfo import RoutingInfoTypedDict as RoutingInfoTypedDict
    from codat_lending.models.sales_order_reference import SalesOrderReferenceTypedDict as SalesOrderReferenceTypedDict
    from codat_lending.models.shared.schema_datatype import SchemaDataType as SchemaDataType
    from codat_lending.models.shared.security import Security as Security
    from codat_lending.models.shared.security import SecurityTypedDict as SecurityTypedDict
    from codat_lending.models.shared.servicechargetype import ServiceChargeType as ServiceChargeType
    from codat_lending.models.shared.servicecharge import ServiceChargeTypedDict as ServiceChargeTypedDict
    from codat_lending.models.source import Source as Source
    from codat_lending.models.shared.sourceaccountprototype import SourceAccountPrototypeTypedDict as SourceAccountPrototypeTypedDict
    from codat_lending.models.source_account_status import SourceAccountStatus as SourceAccountStatus
    from codat_lending.models.shared.sourceaccount import SourceAccountTypedDict as SourceAccountTypedDict
    from codat_lending.models.shared.sourceaccountv2 import SourceAccountV2AccountType as SourceAccountV2AccountType
    from codat_lending.models.shared.sourceaccountv2prototype import SourceAccountV2PrototypeTypedDict as SourceAccountV2PrototypeTypedDict
    from codat_lending.models.source_account_v2_status import SourceAccountV2Status as SourceAccountV2Status
    from codat_lending.models.source_account_v2 import SourceAccountV2TypedDict as SourceAccountV2TypedDict
    from codat_lending.models.shared.sourceref import SourceRefTypedDict as SourceRefTypedDict
    from codat_lending.models.start_upload_session_request_data_type import StartUploadSessionRequestDataType as StartUploadSessionRequestDataType
    from codat_lending.models.shared.startuploadsessionrequest import StartUploadSessionRequestTypedDict as StartUploadSessionRequestTypedDict
    from codat_lending.models.shared.status import Status as Status
    from codat_lending.models.shared.supplementaldata import SupplementalDataTypedDict as SupplementalDataTypedDict
    from codat_lending.models.shared.supplierref import SupplierRefTypedDict as SupplierRefTypedDict
    from codat_lending.models.shared.supplierstatus import SupplierStatus as SupplierStatus
    from codat_lending.models.shared.targetaccountoption import TargetAccountOptionTypedDict as TargetAccountOptionTypedDict
    from codat_lending.models.shared.taxcomponentallocation import TaxComponentAllocationTypedDict as TaxComponentAllocationTypedDict
    from codat_lending.models.shared.taxcomponentref import TaxComponentRefTypedDict as TaxComponentRefTypedDict
    from codat_lending.models.shared.taxrateref import TaxRateRefTypedDict as TaxRateRefTypedDict
    from codat_lending.models.tax_rate_reference import TaxRateReferenceTypedDict as TaxRateReferenceTypedDict
    from codat_lending.models.shared.trackingcategoryref import TrackingCategoryRefTypedDict as TrackingCategoryRefTypedDict
    from codat_lending.models.shared.trackingrecordref import TrackingRecordRefDataType as TrackingRecordRefDataType
    from codat_lending.models.tracking_record_ref import TrackingRecordRefTypedDict as TrackingRecordRefTypedDict
    from codat_lending.models.shared.tracking import TrackingTypedDict as TrackingTypedDict
    from codat_lending.models.shared.transactioncategoryref import TransactionCategoryRefTypedDict as TransactionCategoryRefTypedDict
    from codat_lending.models.shared.transactioncategorystatus import TransactionCategoryStatus as TransactionCategoryStatus
    from codat_lending.models.shared.transactioncategory import TransactionCategoryTypedDict as TransactionCategoryTypedDict
    from codat_lending.models.shared.transactioncode import TransactionCode as TransactionCode
    from codat_lending.models.shared.transactionsourceref import TransactionSourceRefTypedDict as TransactionSourceRefTypedDict
    from codat_lending.models.shared.transactionsourcetype import TransactionSourceType as TransactionSourceType
    from codat_lending.models.shared.transactiontype import TransactionType as TransactionType
    from codat_lending.models.shared.transferaccount import TransferAccountTypedDict as TransferAccountTypedDict
    from codat_lending.models.type import Type as Type
    from codat_lending.models.valid_data_type_links import ValidDataTypeLinksTypedDict as ValidDataTypeLinksTypedDict
    from codat_lending.models.shared.validationitem import ValidationItemTypedDict as ValidationItemTypedDict
    from codat_lending.models.shared.validation import ValidationTypedDict as ValidationTypedDict
    from codat_lending.models.web_link_type import WebLinkType as WebLinkType
    from codat_lending.models.shared.weblink import WebLinkTypedDict as WebLinkTypedDict
    from codat_lending.models.withholding_tax import WithholdingTaxTypedDict as WithholdingTaxTypedDict
    from codat_lending.models.record_line_reference import RecordLineReference as Zero
    from codat_lending.models.shared.zero import ZeroDataType as ZeroDataType
    from codat_lending.models.record_line_reference import RecordLineReferenceTypedDict as ZeroTypedDict
    from codat_lending.models.shared.reportgenerationpayload import ReportGenerationPayload, ReportGenerationPayloadTypedDict
    from codat_lending.models.shared.schema import Schema, SchemaTypedDict
    from codat_lending.models.accountingcreatebankaccounttransactions import AccountingCreateBankAccountTransactions, AccountingCreateBankAccountTransactionsTypedDict
    from codat_lending.models.shared.fileupload import FileUpload, FileUploadTypedDict
    from codat_lending.models.shared.codatfile import CodatFile, CodatFileTypedDict

_dynamic_imports: dict[str, tuple[str, str]] = {
    'Account': ('codat_lending.models.account', 'Account'),
    'AccountBalance': ('codat_lending.models.shared.accountbalance', 'AccountBalance'),
    'AccountBalanceAmounts': ('codat_lending.models.shared.accountbalanceamounts', 'AccountBalanceAmounts'),
    'AccountBalanceAmountsTypedDict': ('codat_lending.models.shared.accountbalanceamounts', 'AccountBalanceAmountsTypedDict'),
    'AccountBalanceTypedDict': ('codat_lending.models.shared.accountbalance', 'AccountBalanceTypedDict'),
    'AccountCategoriesUpdatedWebhook': ('codat_lending.models.shared.accountcategoriesupdatedwebhook', 'AccountCategoriesUpdatedWebhook'),
    'AccountCategoriesUpdatedWebhookData': ('codat_lending.models.shared.accountcategoriesupdatedwebhookdata', 'AccountCategoriesUpdatedWebhookData'),
    'AccountCategoriesUpdatedWebhookDataTypedDict': ('codat_lending.models.shared.accountcategoriesupdatedwebhookdata', 'AccountCategoriesUpdatedWebhookDataTypedDict'),
    'AccountCategoriesUpdatedWebhookTypedDict': ('codat_lending.models.shared.accountcategoriesupdatedwebhook', 'AccountCategoriesUpdatedWebhookTypedDict'),
    'AccountCategoryLevel': ('codat_lending.models.shared.accountcategorylevel', 'AccountCategoryLevel'),
    'AccountCategoryLevelTypedDict': ('codat_lending.models.shared.accountcategorylevel', 'AccountCategoryLevelTypedDict'),
    'AccountIdentifierType': ('codat_lending.models.shared.accountidentifiertype', 'AccountIdentifierType'),
    'AccountIdentifiers': ('codat_lending.models.shared.accountidentifiers', 'AccountIdentifiers'),
    'AccountIdentifiersTypedDict': ('codat_lending.models.shared.accountidentifiers', 'AccountIdentifiersTypedDict'),
    'AccountInfo': ('codat_lending.models.shared.accountinfo', 'AccountInfo'),
    'AccountInfoTypedDict': ('codat_lending.models.shared.accountinfo', 'AccountInfoTypedDict'),
    'AccountInstitution': ('codat_lending.models.shared.accountinstitution', 'AccountInstitution'),
    'AccountInstitutionTypedDict': ('codat_lending.models.shared.accountinstitution', 'AccountInstitutionTypedDict'),
    'AccountPrototype': ('codat_lending.models.shared.accountprototype', 'AccountPrototype'),
    'AccountPrototypeTypedDict': ('codat_lending.models.shared.accountprototype', 'AccountPrototypeTypedDict'),
    'AccountRef': ('codat_lending.models.shared.accountref', 'AccountRef'),
    'AccountRefTypedDict': ('codat_lending.models.shared.accountref', 'AccountRefTypedDict'),
    'AccountStatus': ('codat_lending.models.shared.accountstatus', 'AccountStatus'),
    'AccountTransactionLine': ('codat_lending.models.shared.accounttransactionline', 'AccountTransactionLine'),
    'AccountTransactionLineRecordRef': ('codat_lending.models.account_transaction_line_record_ref', 'AccountTransactionLineRecordRef'),
    'AccountTransactionLineRecordRefDataType': ('codat_lending.models.shared.accounttransactionlinerecordref', 'AccountTransactionLineRecordRefDataType'),
    'AccountTransactionLineRecordRefTypedDict': ('codat_lending.models.account_transaction_line_record_ref', 'AccountTransactionLineRecordRefTypedDict'),
    'AccountTransactionLineTypedDict': ('codat_lending.models.shared.accounttransactionline', 'AccountTransactionLineTypedDict'),
    'AccountType': ('codat_lending.models.shared.accounttype', 'AccountType'),
    'AccountTypedDict': ('codat_lending.models.account', 'AccountTypedDict'),
    'AccountingAccount': ('codat_lending.models.shared.accountingaccount', 'AccountingAccount'),
    'AccountingAccountTransaction': ('codat_lending.models.shared.accountingaccounttransaction', 'AccountingAccountTransaction'),
    'AccountingAccountTransactionDataType': ('codat_lending.models.accounting_account_transaction_data_type', 'AccountingAccountTransactionDataType'),
    'AccountingAccountTransactionStatus': ('codat_lending.models.accounting_account_transaction_status', 'AccountingAccountTransactionStatus'),
    'AccountingAccountTransactionTypedDict': ('codat_lending.models.shared.accountingaccounttransaction', 'AccountingAccountTransactionTypedDict'),
    'AccountingAccountTransactions': ('codat_lending.models.shared.accountingaccounttransactions', 'AccountingAccountTransactions'),
    'AccountingAccountTransactionsTypedDict': ('codat_lending.models.shared.accountingaccounttransactions', 'AccountingAccountTransactionsTypedDict'),
    'AccountingAccountTypedDict': ('codat_lending.models.shared.accountingaccount', 'AccountingAccountTypedDict'),
    'AccountingAccountValidDataTypeLinks': ('codat_lending.models.valid_data_type_links', 'ValidDataTypeLinks'),
    'AccountingAccountValidDataTypeLinksTypedDict': ('codat_lending.models.valid_data_type_links', 'ValidDataTypeLinksTypedDict'),
    'AccountingAccounts': ('codat_lending.models.shared.accountingaccounts', 'AccountingAccounts'),
    'AccountingAccountsTypedDict': ('codat_lending.models.shared.accountingaccounts', 'AccountingAccountsTypedDict'),
    'AccountingAddress': ('codat_lending.models.shared.accountingaddress', 'AccountingAddress'),
    'AccountingAddressType': ('codat_lending.models.shared.accountingaddresstype', 'AccountingAddressType'),
    'AccountingAddressTypedDict': ('codat_lending.models.shared.accountingaddress', 'AccountingAddressTypedDict'),
    'AccountingAgedCreditorReport': ('codat_lending.models.shared.accountingagedcreditorreport', 'AccountingAgedCreditorReport'),
    'AccountingAgedCreditorReportTypedDict': ('codat_lending.models.shared.accountingagedcreditorreport', 'AccountingAgedCreditorReportTypedDict'),
    'AccountingAgedDebtorReport': ('codat_lending.models.shared.accountingageddebtorreport', 'AccountingAgedDebtorReport'),
    'AccountingAgedDebtorReportTypedDict': ('codat_lending.models.shared.accountingageddebtorreport', 'AccountingAgedDebtorReportTypedDict'),
    'AccountingAttachment': ('codat_lending.models.shared.accountingattachment', 'AccountingAttachment'),
    'AccountingAttachmentTypedDict': ('codat_lending.models.shared.accountingattachment', 'AccountingAttachmentTypedDict'),
    'AccountingBalanceSheet': ('codat_lending.models.shared.accountingbalancesheet', 'AccountingBalanceSheet'),
    'AccountingBalanceSheetTypedDict': ('codat_lending.models.shared.accountingbalancesheet', 'AccountingBalanceSheetTypedDict'),
    'AccountingBankAccount': ('codat_lending.models.shared.accountingbankaccount', 'AccountingBankAccount'),
    'AccountingBankAccountType': ('codat_lending.models.shared.accountingbankaccounttype', 'AccountingBankAccountType'),
    'AccountingBankAccountTypedDict': ('codat_lending.models.shared.accountingbankaccount', 'AccountingBankAccountTypedDict'),
    'AccountingBankAccounts': ('codat_lending.models.shared.accountingbankaccounts', 'AccountingBankAccounts'),
    'AccountingBankAccountsTypedDict': ('codat_lending.models.shared.accountingbankaccounts', 'AccountingBankAccountsTypedDict'),
    'AccountingBankTransaction': ('codat_lending.models.shared.accountingbanktransaction', 'AccountingBankTransaction'),
    'AccountingBankTransactionTypedDict': ('codat_lending.models.shared.accountingbanktransaction', 'AccountingBankTransactionTypedDict'),
    'AccountingBankTransactions': ('codat_lending.models.shared.accountingbanktransactions', 'AccountingBankTransactions'),
    'AccountingBankTransactionsTypedDict': ('codat_lending.models.shared.accountingbanktransactions', 'AccountingBankTransactionsTypedDict'),
    'AccountingBill': ('codat_lending.models.shared.accountingbill', 'AccountingBill'),
    'AccountingBillCreditNote': ('codat_lending.models.shared.accountingbillcreditnote', 'AccountingBillCreditNote'),
    'AccountingBillCreditNoteTypedDict': ('codat_lending.models.shared.accountingbillcreditnote', 'AccountingBillCreditNoteTypedDict'),
    'AccountingBillCreditNotes': ('codat_lending.models.shared.accountingbillcreditnotes', 'AccountingBillCreditNotes'),
    'AccountingBillCreditNotesTypedDict': ('codat_lending.models.shared.accountingbillcreditnotes', 'AccountingBillCreditNotesTypedDict'),
    'AccountingBillPayment': ('codat_lending.models.shared.accountingbillpayment', 'AccountingBillPayment'),
    'AccountingBillPaymentAllOfPaymentMethodRef': ('codat_lending.models.accounting_bill_payment_all_of_payment_method_ref', 'AccountingBillPaymentAllOfPaymentMethodRef'),
    'AccountingBillPaymentAllOfPaymentMethodRefTypedDict': ('codat_lending.models.accounting_bill_payment_all_of_payment_method_ref', 'AccountingBillPaymentAllOfPaymentMethodRefTypedDict'),
    'AccountingBillPaymentAllOfSupplierRef': ('codat_lending.models.accounting_bill_payment_all_of_supplier_ref', 'AccountingBillPaymentAllOfSupplierRef'),
    'AccountingBillPaymentAllOfSupplierRefTypedDict': ('codat_lending.models.accounting_bill_payment_all_of_supplier_ref', 'AccountingBillPaymentAllOfSupplierRefTypedDict'),
    'AccountingBillPaymentTypedDict': ('codat_lending.models.shared.accountingbillpayment', 'AccountingBillPaymentTypedDict'),
    'AccountingBillPayments': ('codat_lending.models.shared.accountingbillpayments', 'AccountingBillPayments'),
    'AccountingBillPaymentsTypedDict': ('codat_lending.models.shared.accountingbillpayments', 'AccountingBillPaymentsTypedDict'),
    'AccountingBillTypedDict': ('codat_lending.models.shared.accountingbill', 'AccountingBillTypedDict'),
    'AccountingBills': ('codat_lending.models.shared.accountingbills', 'AccountingBills'),
    'AccountingBillsTypedDict': ('codat_lending.models.shared.accountingbills', 'AccountingBillsTypedDict'),
    'AccountingCashFlowStatement': ('codat_lending.models.shared.accountingcashflowstatement', 'AccountingCashFlowStatement'),
    'AccountingCashFlowStatementTypedDict': ('codat_lending.models.shared.accountingcashflowstatement', 'AccountingCashFlowStatementTypedDict'),
    'AccountingCompanyInfo': ('codat_lending.models.shared.accountingcompanyinfo', 'AccountingCompanyInfo'),
    'AccountingCompanyInfoTypedDict': ('codat_lending.models.shared.accountingcompanyinfo', 'AccountingCompanyInfoTypedDict'),
    'AccountingCreateAccountResponse': ('codat_lending.models.shared.accountingcreateaccountresponse', 'AccountingCreateAccountResponse'),
    'AccountingCreateAccountResponseAccountingAccount': ('codat_lending.models.accounting_create_account_response_all_of_data', 'AccountingCreateAccountResponseAllOfData'),
    'AccountingCreateAccountResponseAccountingAccountTypedDict': ('codat_lending.models.accounting_create_account_response_all_of_data', 'AccountingCreateAccountResponseAllOfData'),
    'AccountingCreateAccountResponseAllOfData': ('codat_lending.models.accounting_create_account_response_all_of_data', 'AccountingCreateAccountResponseAllOfData'),
    'AccountingCreateAccountResponseAllOfDataTypedDict': ('codat_lending.models.accounting_create_account_response_all_of_data', 'AccountingCreateAccountResponseAllOfDataTypedDict'),
    'AccountingCreateAccountResponseTypedDict': ('codat_lending.models.shared.accountingcreateaccountresponse', 'AccountingCreateAccountResponseTypedDict'),
    'AccountingCreateAccountResponseValidDataTypeLinks': ('codat_lending.models.valid_data_type_links', 'ValidDataTypeLinks'),
    'AccountingCreateAccountResponseValidDataTypeLinksTypedDict': ('codat_lending.models.valid_data_type_links', 'ValidDataTypeLinksTypedDict'),
    'AccountingCreateBankAccountResponse': ('codat_lending.models.shared.accountingcreatebankaccountresponse', 'AccountingCreateBankAccountResponse'),
    'AccountingCreateBankAccountResponseAccountingBankAccount': ('codat_lending.models.accounting_create_bank_account_response_all_of_data', 'AccountingCreateBankAccountResponseAllOfData'),
    'AccountingCreateBankAccountResponseAccountingBankAccountTypedDict': ('codat_lending.models.accounting_create_bank_account_response_all_of_data', 'AccountingCreateBankAccountResponseAllOfData'),
    'AccountingCreateBankAccountResponseAllOfData': ('codat_lending.models.accounting_create_bank_account_response_all_of_data', 'AccountingCreateBankAccountResponseAllOfData'),
    'AccountingCreateBankAccountResponseAllOfDataTypedDict': ('codat_lending.models.accounting_create_bank_account_response_all_of_data', 'AccountingCreateBankAccountResponseAllOfDataTypedDict'),
    'AccountingCreateBankAccountResponseTypedDict': ('codat_lending.models.shared.accountingcreatebankaccountresponse', 'AccountingCreateBankAccountResponseTypedDict'),
    'AccountingCreateBankAccountTransactions': ('codat_lending.models.accountingcreatebankaccounttransactions', 'AccountingCreateBankAccountTransactions'),
    'AccountingCreateBankAccountTransactionsTypedDict': ('codat_lending.models.accountingcreatebankaccounttransactions', 'AccountingCreateBankAccountTransactionsTypedDict'),
    'AccountingCreateBankTransactions': ('codat_lending.models.shared.accountingcreatebanktransactions', 'AccountingCreateBankTransactions'),
    'AccountingCreateBankTransactionsResponse': ('codat_lending.models.shared.accountingcreatebanktransactionsresponse', 'AccountingCreateBankTransactionsResponse'),
    'AccountingCreateBankTransactionsResponseAllOfData': ('codat_lending.models.accounting_create_bank_transactions_response_all_of_data', 'AccountingCreateBankTransactionsResponseAllOfData'),
    'AccountingCreateBankTransactionsResponseAllOfDataTypedDict': ('codat_lending.models.accounting_create_bank_transactions_response_all_of_data', 'AccountingCreateBankTransactionsResponseAllOfDataTypedDict'),
    'AccountingCreateBankTransactionsResponseTypedDict': ('codat_lending.models.shared.accountingcreatebanktransactionsresponse', 'AccountingCreateBankTransactionsResponseTypedDict'),
    'AccountingCreateBankTransactionsTypedDict': ('codat_lending.models.shared.accountingcreatebanktransactions', 'AccountingCreateBankTransactionsTypedDict'),
    'AccountingCreateDirectCostResponse': ('codat_lending.models.shared.accountingcreatedirectcostresponse', 'AccountingCreateDirectCostResponse'),
    'AccountingCreateDirectCostResponseAccountingDirectCost': ('codat_lending.models.accounting_create_direct_cost_response_all_of_data', 'AccountingCreateDirectCostResponseAllOfData'),
    'AccountingCreateDirectCostResponseAccountingDirectCostTypedDict': ('codat_lending.models.accounting_create_direct_cost_response_all_of_data', 'AccountingCreateDirectCostResponseAllOfData'),
    'AccountingCreateDirectCostResponseAllOfData': ('codat_lending.models.accounting_create_direct_cost_response_all_of_data', 'AccountingCreateDirectCostResponseAllOfData'),
    'AccountingCreateDirectCostResponseAllOfDataTypedDict': ('codat_lending.models.accounting_create_direct_cost_response_all_of_data', 'AccountingCreateDirectCostResponseAllOfDataTypedDict'),
    'AccountingCreateDirectCostResponseTypedDict': ('codat_lending.models.shared.accountingcreatedirectcostresponse', 'AccountingCreateDirectCostResponseTypedDict'),
    'AccountingCreatePaymentResponse': ('codat_lending.models.shared.accountingcreatepaymentresponse', 'AccountingCreatePaymentResponse'),
    'AccountingCreatePaymentResponseAccountingPayment': ('codat_lending.models.accounting_create_payment_response_all_of_data', 'AccountingCreatePaymentResponseAllOfData'),
    'AccountingCreatePaymentResponseAccountingPaymentTypedDict': ('codat_lending.models.accounting_create_payment_response_all_of_data', 'AccountingCreatePaymentResponseAllOfData'),
    'AccountingCreatePaymentResponseAllOfData': ('codat_lending.models.accounting_create_payment_response_all_of_data', 'AccountingCreatePaymentResponseAllOfData'),
    'AccountingCreatePaymentResponseAllOfDataTypedDict': ('codat_lending.models.accounting_create_payment_response_all_of_data', 'AccountingCreatePaymentResponseAllOfDataTypedDict'),
    'AccountingCreatePaymentResponseTypedDict': ('codat_lending.models.shared.accountingcreatepaymentresponse', 'AccountingCreatePaymentResponseTypedDict'),
    'AccountingCreateSupplierResponse': ('codat_lending.models.shared.accountingcreatesupplierresponse', 'AccountingCreateSupplierResponse'),
    'AccountingCreateSupplierResponseAccountingSupplier': ('codat_lending.models.accounting_create_supplier_response_all_of_data', 'AccountingCreateSupplierResponseAllOfData'),
    'AccountingCreateSupplierResponseAccountingSupplierTypedDict': ('codat_lending.models.accounting_create_supplier_response_all_of_data', 'AccountingCreateSupplierResponseAllOfData'),
    'AccountingCreateSupplierResponseAllOfData': ('codat_lending.models.accounting_create_supplier_response_all_of_data', 'AccountingCreateSupplierResponseAllOfData'),
    'AccountingCreateSupplierResponseAllOfDataTypedDict': ('codat_lending.models.accounting_create_supplier_response_all_of_data', 'AccountingCreateSupplierResponseAllOfDataTypedDict'),
    'AccountingCreateSupplierResponseTypedDict': ('codat_lending.models.shared.accountingcreatesupplierresponse', 'AccountingCreateSupplierResponseTypedDict'),
    'AccountingCreateTransferResponse': ('codat_lending.models.accounting_create_transfer_response', 'AccountingCreateTransferResponse'),
    'AccountingCreateTransferResponseAccountingTransfer': ('codat_lending.models.accounting_create_transfer_response_all_of_data', 'AccountingCreateTransferResponseAllOfData'),
    'AccountingCreateTransferResponseAccountingTransferTypedDict': ('codat_lending.models.accounting_create_transfer_response_all_of_data', 'AccountingCreateTransferResponseAllOfData'),
    'AccountingCreateTransferResponseAllOfData': ('codat_lending.models.accounting_create_transfer_response_all_of_data', 'AccountingCreateTransferResponseAllOfData'),
    'AccountingCreateTransferResponseAllOfDataTypedDict': ('codat_lending.models.accounting_create_transfer_response_all_of_data', 'AccountingCreateTransferResponseAllOfDataTypedDict'),
    'AccountingCreateTransferResponseStatus': ('codat_lending.models.shared.accountingcreatetransferresponse', 'AccountingCreateTransferResponseStatus'),
    'AccountingCreateTransferResponseTypedDict': ('codat_lending.models.accounting_create_transfer_response', 'AccountingCreateTransferResponseTypedDict'),
    'AccountingCreditNote': ('codat_lending.models.shared.accountingcreditnote', 'AccountingCreditNote'),
    'AccountingCreditNoteTypedDict': ('codat_lending.models.shared.accountingcreditnote', 'AccountingCreditNoteTypedDict'),
    'AccountingCreditNotes': ('codat_lending.models.shared.accountingcreditnotes', 'AccountingCreditNotes'),
    'AccountingCreditNotesTypedDict': ('codat_lending.models.shared.accountingcreditnotes', 'AccountingCreditNotesTypedDict'),
    'AccountingCustomer': ('codat_lending.models.shared.accountingcustomer', 'AccountingCustomer'),
    'AccountingCustomerRef': ('codat_lending.models.shared.accountingcustomerref', 'AccountingCustomerRef'),
    'AccountingCustomerRefTypedDict': ('codat_lending.models.shared.accountingcustomerref', 'AccountingCustomerRefTypedDict'),
    'AccountingCustomerTypedDict': ('codat_lending.models.shared.accountingcustomer', 'AccountingCustomerTypedDict'),
    'AccountingCustomers': ('codat_lending.models.shared.accountingcustomers', 'AccountingCustomers'),
    'AccountingCustomersTypedDict': ('codat_lending.models.shared.accountingcustomers', 'AccountingCustomersTypedDict'),
    'AccountingDirectCost': ('codat_lending.models.shared.accountingdirectcost', 'AccountingDirectCost'),
    'AccountingDirectCostTypedDict': ('codat_lending.models.shared.accountingdirectcost', 'AccountingDirectCostTypedDict'),
    'AccountingDirectCosts': ('codat_lending.models.shared.accountingdirectcosts', 'AccountingDirectCosts'),
    'AccountingDirectCostsTypedDict': ('codat_lending.models.shared.accountingdirectcosts', 'AccountingDirectCostsTypedDict'),
    'AccountingDirectIncome': ('codat_lending.models.shared.accountingdirectincome', 'AccountingDirectIncome'),
    'AccountingDirectIncomeTypedDict': ('codat_lending.models.shared.accountingdirectincome', 'AccountingDirectIncomeTypedDict'),
    'AccountingDirectIncomes': ('codat_lending.models.shared.accountingdirectincomes', 'AccountingDirectIncomes'),
    'AccountingDirectIncomesTypedDict': ('codat_lending.models.shared.accountingdirectincomes', 'AccountingDirectIncomesTypedDict'),
    'AccountingInvoice': ('codat_lending.models.shared.accountinginvoice', 'AccountingInvoice'),
    'AccountingInvoiceDataType': ('codat_lending.models.accounting_invoice_data_type', 'AccountingInvoiceDataType'),
    'AccountingInvoiceTypedDict': ('codat_lending.models.shared.accountinginvoice', 'AccountingInvoiceTypedDict'),
    'AccountingInvoices': ('codat_lending.models.shared.accountinginvoices', 'AccountingInvoices'),
    'AccountingInvoicesTypedDict': ('codat_lending.models.shared.accountinginvoices', 'AccountingInvoicesTypedDict'),
    'AccountingJournal': ('codat_lending.models.shared.accountingjournal', 'AccountingJournal'),
    'AccountingJournalEntries': ('codat_lending.models.shared.accountingjournalentries', 'AccountingJournalEntries'),
    'AccountingJournalEntriesTypedDict': ('codat_lending.models.shared.accountingjournalentries', 'AccountingJournalEntriesTypedDict'),
    'AccountingJournalEntry': ('codat_lending.models.shared.accountingjournalentry', 'AccountingJournalEntry'),
    'AccountingJournalEntryDataType': ('codat_lending.models.accounting_journal_entry_data_type', 'AccountingJournalEntryDataType'),
    'AccountingJournalEntryTypedDict': ('codat_lending.models.shared.accountingjournalentry', 'AccountingJournalEntryTypedDict'),
    'AccountingJournalTypedDict': ('codat_lending.models.shared.accountingjournal', 'AccountingJournalTypedDict'),
    'AccountingJournals': ('codat_lending.models.shared.accountingjournals', 'AccountingJournals'),
    'AccountingJournalsTypedDict': ('codat_lending.models.shared.accountingjournals', 'AccountingJournalsTypedDict'),
    'AccountingPayment': ('codat_lending.models.shared.accountingpayment', 'AccountingPayment'),
    'AccountingPaymentAllocation': ('codat_lending.models.shared.accountingpaymentallocation', 'AccountingPaymentAllocation'),
    'AccountingPaymentAllocationAllocation': ('codat_lending.models.accounting_payment_allocation_allocation', 'AccountingPaymentAllocationAllocation'),
    'AccountingPaymentAllocationAllocationTypedDict': ('codat_lending.models.accounting_payment_allocation_allocation', 'AccountingPaymentAllocationAllocationTypedDict'),
    'AccountingPaymentAllocationTypedDict': ('codat_lending.models.shared.accountingpaymentallocation', 'AccountingPaymentAllocationTypedDict'),
    'AccountingPaymentMethod': ('codat_lending.models.accounting_payment_method', 'AccountingPaymentMethod'),
    'AccountingPaymentMethodTypedDict': ('codat_lending.models.accounting_payment_method', 'AccountingPaymentMethodTypedDict'),
    'AccountingPaymentTypedDict': ('codat_lending.models.shared.accountingpayment', 'AccountingPaymentTypedDict'),
    'AccountingPayments': ('codat_lending.models.shared.accountingpayments', 'AccountingPayments'),
    'AccountingPaymentsTypedDict': ('codat_lending.models.shared.accountingpayments', 'AccountingPaymentsTypedDict'),
    'AccountingProfitAndLossReport': ('codat_lending.models.shared.accountingprofitandlossreport', 'AccountingProfitAndLossReport'),
    'AccountingProfitAndLossReportTypedDict': ('codat_lending.models.shared.accountingprofitandlossreport', 'AccountingProfitAndLossReportTypedDict'),
    'AccountingRecordRef': ('codat_lending.models.shared.accountingrecordref', 'AccountingRecordRef'),
    'AccountingRecordRefTypedDict': ('codat_lending.models.shared.accountingrecordref', 'AccountingRecordRefTypedDict'),
    'AccountingSupplier': ('codat_lending.models.shared.accountingsupplier', 'AccountingSupplier'),
    'AccountingSupplierTypedDict': ('codat_lending.models.shared.accountingsupplier', 'AccountingSupplierTypedDict'),
    'AccountingSuppliers': ('codat_lending.models.shared.accountingsuppliers', 'AccountingSuppliers'),
    'AccountingSuppliersTypedDict': ('codat_lending.models.shared.accountingsuppliers', 'AccountingSuppliersTypedDict'),
    'AccountingTrackingCategory': ('codat_lending.models.accounting_tracking_category', 'AccountingTrackingCategory'),
    'AccountingTrackingCategoryTypedDict': ('codat_lending.models.accounting_tracking_category', 'AccountingTrackingCategoryTypedDict'),
    'AccountingTransfer': ('codat_lending.models.shared.accountingtransfer', 'AccountingTransfer'),
    'AccountingTransferStatus': ('codat_lending.models.accounting_transfer_status', 'AccountingTransferStatus'),
    'AccountingTransferTypedDict': ('codat_lending.models.shared.accountingtransfer', 'AccountingTransferTypedDict'),
    'AccountingTransfers': ('codat_lending.models.shared.accountingtransfers', 'AccountingTransfers'),
    'AccountingTransfersTypedDict': ('codat_lending.models.shared.accountingtransfers', 'AccountingTransfersTypedDict'),
    'Accounts': ('codat_lending.models.shared.accounts', 'Accounts'),
    'AccountsPayableTracking': ('codat_lending.models.shared.accountspayabletracking', 'AccountsPayableTracking'),
    'AccountsPayableTrackingTypedDict': ('codat_lending.models.shared.accountspayabletracking', 'AccountsPayableTrackingTypedDict'),
    'AccountsReceivableTracking': ('codat_lending.models.shared.accountsreceivabletracking', 'AccountsReceivableTracking'),
    'AccountsReceivableTrackingTypedDict': ('codat_lending.models.shared.accountsreceivabletracking', 'AccountsReceivableTrackingTypedDict'),
    'AccountsTypedDict': ('codat_lending.models.shared.accounts', 'AccountsTypedDict'),
    'AgedCreditor': ('codat_lending.models.shared.agedcreditor', 'AgedCreditor'),
    'AgedCreditorTypedDict': ('codat_lending.models.shared.agedcreditor', 'AgedCreditorTypedDict'),
    'AgedCurrencyOutstanding': ('codat_lending.models.shared.agedcurrencyoutstanding', 'AgedCurrencyOutstanding'),
    'AgedCurrencyOutstandingTypedDict': ('codat_lending.models.shared.agedcurrencyoutstanding', 'AgedCurrencyOutstandingTypedDict'),
    'AgedDebtor': ('codat_lending.models.shared.ageddebtor', 'AgedDebtor'),
    'AgedDebtorTypedDict': ('codat_lending.models.shared.ageddebtor', 'AgedDebtorTypedDict'),
    'AgedOutstandingAmount': ('codat_lending.models.shared.agedoutstandingamount', 'AgedOutstandingAmount'),
    'AgedOutstandingAmountDetail': ('codat_lending.models.shared.agedoutstandingamountdetail', 'AgedOutstandingAmountDetail'),
    'AgedOutstandingAmountDetailTypedDict': ('codat_lending.models.shared.agedoutstandingamountdetail', 'AgedOutstandingAmountDetailTypedDict'),
    'AgedOutstandingAmountTypedDict': ('codat_lending.models.shared.agedoutstandingamount', 'AgedOutstandingAmountTypedDict'),
    'Allocation': ('codat_lending.models.accounting_payment_allocation_allocation', 'AccountingPaymentAllocationAllocation'),
    'AllocationTypedDict': ('codat_lending.models.accounting_payment_allocation_allocation', 'AccountingPaymentAllocationAllocationTypedDict'),
    'Attachments': ('codat_lending.models.shared.attachments', 'Attachments'),
    'AttachmentsTypedDict': ('codat_lending.models.shared.attachments', 'AttachmentsTypedDict'),
    'BalanceSheet': ('codat_lending.models.shared.balancesheet', 'BalanceSheet'),
    'BalanceSheetTypedDict': ('codat_lending.models.shared.balancesheet', 'BalanceSheetTypedDict'),
    'BankAccountPrototype': ('codat_lending.models.bank_account_prototype', 'BankAccountPrototype'),
    'BankAccountPrototypeTypedDict': ('codat_lending.models.bank_account_prototype', 'BankAccountPrototypeTypedDict'),
    'BankAccountRef': ('codat_lending.models.shared.bankaccountref', 'BankAccountRef'),
    'BankAccountRefTypedDict': ('codat_lending.models.shared.bankaccountref', 'BankAccountRefTypedDict'),
    'BankAccountStatus': ('codat_lending.models.shared.bankaccountstatus', 'BankAccountStatus'),
    'BankFeedBankAccountMapping': ('codat_lending.models.shared.bankfeedbankaccountmapping', 'BankFeedBankAccountMapping'),
    'BankFeedBankAccountMappingResponse': ('codat_lending.models.shared.bankfeedbankaccountmappingresponse', 'BankFeedBankAccountMappingResponse'),
    'BankFeedBankAccountMappingResponseTypedDict': ('codat_lending.models.shared.bankfeedbankaccountmappingresponse', 'BankFeedBankAccountMappingResponseTypedDict'),
    'BankFeedBankAccountMappingTypedDict': ('codat_lending.models.shared.bankfeedbankaccountmapping', 'BankFeedBankAccountMappingTypedDict'),
    'BankFeedMapping': ('codat_lending.models.shared.bankfeedmapping', 'BankFeedMapping'),
    'BankFeedMappingTypedDict': ('codat_lending.models.shared.bankfeedmapping', 'BankFeedMappingTypedDict'),
    'BankStatementUploadConfiguration': ('codat_lending.models.shared.bankstatementuploadconfiguration', 'BankStatementUploadConfiguration'),
    'BankStatementUploadConfigurationTypedDict': ('codat_lending.models.shared.bankstatementuploadconfiguration', 'BankStatementUploadConfigurationTypedDict'),
    'BankTransactionType': ('codat_lending.models.shared.banktransactiontype', 'BankTransactionType'),
    'BankingAccount': ('codat_lending.models.shared.bankingaccount', 'BankingAccount'),
    'BankingAccountBalance': ('codat_lending.models.shared.bankingaccountbalance', 'BankingAccountBalance'),
    'BankingAccountBalanceTypedDict': ('codat_lending.models.shared.bankingaccountbalance', 'BankingAccountBalanceTypedDict'),
    'BankingAccountBalances': ('codat_lending.models.shared.bankingaccountbalances', 'BankingAccountBalances'),
    'BankingAccountBalancesTypedDict': ('codat_lending.models.shared.bankingaccountbalances', 'BankingAccountBalancesTypedDict'),
    'BankingAccountTypedDict': ('codat_lending.models.shared.bankingaccount', 'BankingAccountTypedDict'),
    'BankingAccounts': ('codat_lending.models.shared.bankingaccounts', 'BankingAccounts'),
    'BankingAccountsTypedDict': ('codat_lending.models.shared.bankingaccounts', 'BankingAccountsTypedDict'),
    'BankingTransaction': ('codat_lending.models.shared.bankingtransaction', 'BankingTransaction'),
    'BankingTransactionCategories': ('codat_lending.models.shared.bankingtransactioncategories', 'BankingTransactionCategories'),
    'BankingTransactionCategoriesTypedDict': ('codat_lending.models.shared.bankingtransactioncategories', 'BankingTransactionCategoriesTypedDict'),
    'BankingTransactionCategory': ('codat_lending.models.shared.bankingtransactioncategory', 'BankingTransactionCategory'),
    'BankingTransactionCategoryTypedDict': ('codat_lending.models.shared.bankingtransactioncategory', 'BankingTransactionCategoryTypedDict'),
    'BankingTransactionRef': ('codat_lending.models.shared.bankingtransactionref', 'BankingTransactionRef'),
    'BankingTransactionRefTypedDict': ('codat_lending.models.shared.bankingtransactionref', 'BankingTransactionRefTypedDict'),
    'BankingTransactionTypedDict': ('codat_lending.models.shared.bankingtransaction', 'BankingTransactionTypedDict'),
    'BankingTransactions': ('codat_lending.models.shared.bankingtransactions', 'BankingTransactions'),
    'BankingTransactionsTypedDict': ('codat_lending.models.shared.bankingtransactions', 'BankingTransactionsTypedDict'),
    'BillCreditNoteLineItem': ('codat_lending.models.shared.billcreditnotelineitem', 'BillCreditNoteLineItem'),
    'BillCreditNoteLineItemTypedDict': ('codat_lending.models.shared.billcreditnotelineitem', 'BillCreditNoteLineItemTypedDict'),
    'BillCreditNoteStatus': ('codat_lending.models.shared.billcreditnotestatus', 'BillCreditNoteStatus'),
    'BillLineItem': ('codat_lending.models.bill_line_item', 'BillLineItem'),
    'BillLineItemDataType': ('codat_lending.models.shared.billlineitem', 'BillLineItemDataType'),
    'BillLineItemPurchaseOrderLineRef': ('codat_lending.models.bill_line_item_purchase_order_line_ref', 'BillLineItemPurchaseOrderLineRef'),
    'BillLineItemPurchaseOrderLineRefDataType': ('codat_lending.models.bill_line_item_purchase_order_line_ref_data_type', 'BillLineItemPurchaseOrderLineRefDataType'),
    'BillLineItemPurchaseOrderLineRefTypedDict': ('codat_lending.models.bill_line_item_purchase_order_line_ref', 'BillLineItemPurchaseOrderLineRefTypedDict'),
    'BillLineItemTypedDict': ('codat_lending.models.bill_line_item', 'BillLineItemTypedDict'),
    'BillPaymentLine': ('codat_lending.models.shared.billpaymentline', 'BillPaymentLine'),
    'BillPaymentLineLink': ('codat_lending.models.shared.billpaymentlinelink', 'BillPaymentLineLink'),
    'BillPaymentLineLinkType': ('codat_lending.models.shared.billpaymentlinelinktype', 'BillPaymentLineLinkType'),
    'BillPaymentLineLinkTypedDict': ('codat_lending.models.shared.billpaymentlinelink', 'BillPaymentLineLinkTypedDict'),
    'BillPaymentLineTypedDict': ('codat_lending.models.shared.billpaymentline', 'BillPaymentLineTypedDict'),
    'BillStatus': ('codat_lending.models.shared.billstatus', 'BillStatus'),
    'BilledToType': ('codat_lending.models.shared.billedtotype', 'BilledToType'),
    'BilledToType1': ('codat_lending.models.shared.billedtotype1', 'BilledToType1'),
    'CashFlowStatement': ('codat_lending.models.shared.cashflowstatement', 'CashFlowStatement'),
    'CashFlowStatementTypedDict': ('codat_lending.models.shared.cashflowstatement', 'CashFlowStatementTypedDict'),
    'CashFlowTransaction': ('codat_lending.models.cash_flow_transaction', 'CashFlowTransaction'),
    'CashFlowTransactionTypedDict': ('codat_lending.models.cash_flow_transaction', 'CashFlowTransactionTypedDict'),
    'CategorizedBankStatementAccounts': ('codat_lending.models.categorized_bank_statement_accounts', 'CategorizedBankStatementAccounts'),
    'CategorizedBankStatementAccountsTypedDict': ('codat_lending.models.categorized_bank_statement_accounts', 'CategorizedBankStatementAccountsTypedDict'),
    'CategorizedBankStatementTransactions': ('codat_lending.models.categorized_bank_statement_transactions', 'CategorizedBankStatementTransactions'),
    'CategorizedBankStatementTransactionsTypedDict': ('codat_lending.models.categorized_bank_statement_transactions', 'CategorizedBankStatementTransactionsTypedDict'),
    'ClientRateLimitWebhook': ('codat_lending.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhook'),
    'ClientRateLimitWebhookPayload': ('codat_lending.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayload'),
    'ClientRateLimitWebhookPayloadTypedDict': ('codat_lending.models.shared.clientratelimitwebhookpayload', 'ClientRateLimitWebhookPayloadTypedDict'),
    'ClientRateLimitWebhookTypedDict': ('codat_lending.models.shared.clientratelimitwebhook', 'ClientRateLimitWebhookTypedDict'),
    'CodatFile': ('codat_lending.models.shared.codatfile', 'CodatFile'),
    'CodatFileTypedDict': ('codat_lending.models.shared.codatfile', 'CodatFileTypedDict'),
    'CommerceAddress': ('codat_lending.models.shared.commerceaddress', 'CommerceAddress'),
    'CommerceAddressType': ('codat_lending.models.shared.commerceaddresstype', 'CommerceAddressType'),
    'CommerceAddressTypedDict': ('codat_lending.models.shared.commerceaddress', 'CommerceAddressTypedDict'),
    'CommerceCompanyInfo': ('codat_lending.models.shared.commercecompanyinfo', 'CommerceCompanyInfo'),
    'CommerceCompanyInfoTypedDict': ('codat_lending.models.shared.commercecompanyinfo', 'CommerceCompanyInfoTypedDict'),
    'CommerceCustomer': ('codat_lending.models.shared.commercecustomer', 'CommerceCustomer'),
    'CommerceCustomerRef': ('codat_lending.models.shared.commercecustomerref', 'CommerceCustomerRef'),
    'CommerceCustomerRefTypedDict': ('codat_lending.models.shared.commercecustomerref', 'CommerceCustomerRefTypedDict'),
    'CommerceCustomerTypedDict': ('codat_lending.models.shared.commercecustomer', 'CommerceCustomerTypedDict'),
    'CommerceCustomers': ('codat_lending.models.shared.commercecustomers', 'CommerceCustomers'),
    'CommerceCustomersTypedDict': ('codat_lending.models.shared.commercecustomers', 'CommerceCustomersTypedDict'),
    'CommerceDispute': ('codat_lending.models.shared.commercedispute', 'CommerceDispute'),
    'CommerceDisputeTypedDict': ('codat_lending.models.shared.commercedispute', 'CommerceDisputeTypedDict'),
    'CommerceDisputes': ('codat_lending.models.shared.commercedisputes', 'CommerceDisputes'),
    'CommerceDisputesTypedDict': ('codat_lending.models.shared.commercedisputes', 'CommerceDisputesTypedDict'),
    'CommerceLocation': ('codat_lending.models.shared.commercelocation', 'CommerceLocation'),
    'CommerceLocationTypedDict': ('codat_lending.models.shared.commercelocation', 'CommerceLocationTypedDict'),
    'CommerceLocations': ('codat_lending.models.shared.commercelocations', 'CommerceLocations'),
    'CommerceLocationsTypedDict': ('codat_lending.models.shared.commercelocations', 'CommerceLocationsTypedDict'),
    'CommerceOrder': ('codat_lending.models.shared.commerceorder', 'CommerceOrder'),
    'CommerceOrderTypedDict': ('codat_lending.models.shared.commerceorder', 'CommerceOrderTypedDict'),
    'CommerceOrders': ('codat_lending.models.shared.commerceorders', 'CommerceOrders'),
    'CommerceOrdersTypedDict': ('codat_lending.models.shared.commerceorders', 'CommerceOrdersTypedDict'),
    'CommercePayment': ('codat_lending.models.shared.commercepayment', 'CommercePayment'),
    'CommercePaymentMethod': ('codat_lending.models.shared.commercepaymentmethod', 'CommercePaymentMethod'),
    'CommercePaymentMethodStatus': ('codat_lending.models.commerce_payment_method_status', 'CommercePaymentMethodStatus'),
    'CommercePaymentMethodTypedDict': ('codat_lending.models.shared.commercepaymentmethod', 'CommercePaymentMethodTypedDict'),
    'CommercePaymentMethods': ('codat_lending.models.shared.commercepaymentmethods', 'CommercePaymentMethods'),
    'CommercePaymentMethodsTypedDict': ('codat_lending.models.shared.commercepaymentmethods', 'CommercePaymentMethodsTypedDict'),
    'CommercePaymentTypedDict': ('codat_lending.models.shared.commercepayment', 'CommercePaymentTypedDict'),
    'CommercePayments': ('codat_lending.models.shared.commercepayments', 'CommercePayments'),
    'CommercePaymentsTypedDict': ('codat_lending.models.shared.commercepayments', 'CommercePaymentsTypedDict'),
    'CommerceProduct': ('codat_lending.models.shared.commerceproduct', 'CommerceProduct'),
    'CommerceProductCategories': ('codat_lending.models.shared.commerceproductcategories', 'CommerceProductCategories'),
    'CommerceProductCategoriesTypedDict': ('codat_lending.models.shared.commerceproductcategories', 'CommerceProductCategoriesTypedDict'),
    'CommerceProductCategory': ('codat_lending.models.shared.commerceproductcategory', 'CommerceProductCategory'),
    'CommerceProductCategoryTypedDict': ('codat_lending.models.shared.commerceproductcategory', 'CommerceProductCategoryTypedDict'),
    'CommerceProductTypedDict': ('codat_lending.models.shared.commerceproduct', 'CommerceProductTypedDict'),
    'CommerceProducts': ('codat_lending.models.shared.commerceproducts', 'CommerceProducts'),
    'CommerceProductsTypedDict': ('codat_lending.models.shared.commerceproducts', 'CommerceProductsTypedDict'),
    'CommerceRecordRef': ('codat_lending.models.shared.commercerecordref', 'CommerceRecordRef'),
    'CommerceRecordRefTypedDict': ('codat_lending.models.shared.commercerecordref', 'CommerceRecordRefTypedDict'),
    'CommerceReport': ('codat_lending.models.shared.commercereport', 'CommerceReport'),
    'CommerceReportComponent': ('codat_lending.models.shared.commercereportcomponent', 'CommerceReportComponent'),
    'CommerceReportComponentTypedDict': ('codat_lending.models.shared.commercereportcomponent', 'CommerceReportComponentTypedDict'),
    'CommerceReportDimension': ('codat_lending.models.shared.commercereportdimension', 'CommerceReportDimension'),
    'CommerceReportDimensionItems': ('codat_lending.models.commerce_report_dimension_items', 'CommerceReportDimensionItems'),
    'CommerceReportDimensionItemsTypedDict': ('codat_lending.models.commerce_report_dimension_items', 'CommerceReportDimensionItemsTypedDict'),
    'CommerceReportDimensionTypedDict': ('codat_lending.models.shared.commercereportdimension', 'CommerceReportDimensionTypedDict'),
    'CommerceReportError': ('codat_lending.models.shared.commercereporterror', 'CommerceReportError'),
    'CommerceReportErrorTypedDict': ('codat_lending.models.shared.commercereporterror', 'CommerceReportErrorTypedDict'),
    'CommerceReportMeasure': ('codat_lending.models.shared.commercereportmeasure', 'CommerceReportMeasure'),
    'CommerceReportMeasureTypedDict': ('codat_lending.models.shared.commercereportmeasure', 'CommerceReportMeasureTypedDict'),
    'CommerceReportTypedDict': ('codat_lending.models.shared.commercereport', 'CommerceReportTypedDict'),
    'CommerceTaxComponent': ('codat_lending.models.commerce_tax_component', 'CommerceTaxComponent'),
    'CommerceTaxComponentTypedDict': ('codat_lending.models.commerce_tax_component', 'CommerceTaxComponentTypedDict'),
    'CommerceTransaction': ('codat_lending.models.shared.commercetransaction', 'CommerceTransaction'),
    'CommerceTransactionTypedDict': ('codat_lending.models.shared.commercetransaction', 'CommerceTransactionTypedDict'),
    'CommerceTransactions': ('codat_lending.models.shared.commercetransactions', 'CommerceTransactions'),
    'CommerceTransactionsTypedDict': ('codat_lending.models.shared.commercetransactions', 'CommerceTransactionsTypedDict'),
    'Companies': ('codat_lending.models.shared.companies', 'Companies'),
    'CompaniesTypedDict': ('codat_lending.models.shared.companies', 'CompaniesTypedDict'),
    'Company': ('codat_lending.models.shared.company', 'Company'),
    'CompanyDetails': ('codat_lending.models.company_details', 'CompanyDetails'),
    'CompanyDetailsTypedDict': ('codat_lending.models.company_details', 'CompanyDetailsTypedDict'),
    'CompanyReference': ('codat_lending.models.shared.companyreference', 'CompanyReference'),
    'CompanyReferenceLinks': ('codat_lending.models.company_reference_links', 'CompanyReferenceLinks'),
    'CompanyReferenceLinksTypedDict': ('codat_lending.models.company_reference_links', 'CompanyReferenceLinksTypedDict'),
    'CompanyReferenceTypedDict': ('codat_lending.models.shared.companyreference', 'CompanyReferenceTypedDict'),
    'CompanyRequestBody': ('codat_lending.models.shared.companyrequestbody', 'CompanyRequestBody'),
    'CompanyRequestBodyTypedDict': ('codat_lending.models.shared.companyrequestbody', 'CompanyRequestBodyTypedDict'),
    'CompanyTypedDict': ('codat_lending.models.shared.company', 'CompanyTypedDict'),
    'CompanyUpdateRequest': ('codat_lending.models.shared.companyupdaterequest', 'CompanyUpdateRequest'),
    'CompanyUpdateRequestTypedDict': ('codat_lending.models.shared.companyupdaterequest', 'CompanyUpdateRequestTypedDict'),
    'Connection': ('codat_lending.models.shared.connection', 'Connection'),
    'ConnectionTypedDict': ('codat_lending.models.shared.connection', 'ConnectionTypedDict'),
    'Connections': ('codat_lending.models.shared.connections', 'Connections'),
    'ConnectionsTypedDict': ('codat_lending.models.shared.connections', 'ConnectionsTypedDict'),
    'Contact': ('codat_lending.models.shared.contact', 'Contact'),
    'ContactRef': ('codat_lending.models.contact_ref', 'ContactRef'),
    'ContactRefDataType': ('codat_lending.models.shared.contactref', 'ContactRefDataType'),
    'ContactRefTypedDict': ('codat_lending.models.contact_ref', 'ContactRefTypedDict'),
    'ContactReference': ('codat_lending.models.contact_reference', 'ContactReference'),
    'ContactReferenceTypedDict': ('codat_lending.models.contact_reference', 'ContactReferenceTypedDict'),
    'ContactTypedDict': ('codat_lending.models.shared.contact', 'ContactTypedDict'),
    'CreateBankAccountTransaction': ('codat_lending.models.shared.createbankaccounttransaction', 'CreateBankAccountTransaction'),
    'CreateBankAccountTransactionTypedDict': ('codat_lending.models.shared.createbankaccounttransaction', 'CreateBankAccountTransactionTypedDict'),
    'CreateConnectionRequest': ('codat_lending.models.create_connection_request', 'CreateConnectionRequest'),
    'CreateConnectionRequestTypedDict': ('codat_lending.models.create_connection_request', 'CreateConnectionRequestTypedDict'),
    'CreateSourceAccount200Response': ('codat_lending.models.create_source_account200_response', 'CreateSourceAccount200Response'),
    'CreateSourceAccount200ResponseTypedDict': ('codat_lending.models.create_source_account200_response', 'CreateSourceAccount200ResponseTypedDict'),
    'CreateSourceAccountRequest': ('codat_lending.models.create_source_account_request', 'CreateSourceAccountRequest'),
    'CreateSourceAccountRequestTypedDict': ('codat_lending.models.create_source_account_request', 'CreateSourceAccountRequestTypedDict'),
    'CreatedDate': ('codat_lending.models.created_date', 'CreatedDate'),
    'CreatedDateTypedDict': ('codat_lending.models.created_date', 'CreatedDateTypedDict'),
    'CreditNoteLineItem': ('codat_lending.models.shared.creditnotelineitem', 'CreditNoteLineItem'),
    'CreditNoteLineItemTypedDict': ('codat_lending.models.shared.creditnotelineitem', 'CreditNoteLineItemTypedDict'),
    'CreditNoteStatus': ('codat_lending.models.shared.creditnotestatus', 'CreditNoteStatus'),
    'CurrentStatus': ('codat_lending.models.current_status', 'CurrentStatus'),
    'CustomerStatus': ('codat_lending.models.shared.customerstatus', 'CustomerStatus'),
    'DataConnectionError': ('codat_lending.models.shared.dataconnectionerror', 'DataConnectionError'),
    'DataConnectionErrorTypedDict': ('codat_lending.models.shared.dataconnectionerror', 'DataConnectionErrorTypedDict'),
    'DataConnectionStatus': ('codat_lending.models.shared.dataconnectionstatus', 'DataConnectionStatus'),
    'DataIntegrityAmounts': ('codat_lending.models.shared.dataintegrityamounts', 'DataIntegrityAmounts'),
    'DataIntegrityAmountsTypedDict': ('codat_lending.models.shared.dataintegrityamounts', 'DataIntegrityAmountsTypedDict'),
    'DataIntegrityByAmount': ('codat_lending.models.shared.dataintegritybyamount', 'DataIntegrityByAmount'),
    'DataIntegrityByAmountTypedDict': ('codat_lending.models.shared.dataintegritybyamount', 'DataIntegrityByAmountTypedDict'),
    'DataIntegrityByCount': ('codat_lending.models.shared.dataintegritybycount', 'DataIntegrityByCount'),
    'DataIntegrityByCountTypedDict': ('codat_lending.models.shared.dataintegritybycount', 'DataIntegrityByCountTypedDict'),
    'DataIntegrityConnectionID': ('codat_lending.models.shared.dataintegrityconnectionid', 'DataIntegrityConnectionId'),
    'DataIntegrityConnectionIDTypedDict': ('codat_lending.models.shared.dataintegrityconnectionid', 'DataIntegrityConnectionIdTypedDict'),
    'DataIntegrityConnectionId': ('codat_lending.models.shared.dataintegrityconnectionid', 'DataIntegrityConnectionId'),
    'DataIntegrityConnectionIdTypedDict': ('codat_lending.models.shared.dataintegrityconnectionid', 'DataIntegrityConnectionIdTypedDict'),
    'DataIntegrityDataType': ('codat_lending.models.shared.dataintegritydatatype', 'DataIntegrityDataType'),
    'DataIntegrityDates': ('codat_lending.models.shared.dataintegritydates', 'DataIntegrityDates'),
    'DataIntegrityDatesTypedDict': ('codat_lending.models.shared.dataintegritydates', 'DataIntegrityDatesTypedDict'),
    'DataIntegrityDetail': ('codat_lending.models.shared.dataintegritydetail', 'DataIntegrityDetail'),
    'DataIntegrityDetailTypedDict': ('codat_lending.models.shared.dataintegritydetail', 'DataIntegrityDetailTypedDict'),
    'DataIntegrityDetails': ('codat_lending.models.shared.dataintegritydetails', 'DataIntegrityDetails'),
    'DataIntegrityDetailsTypedDict': ('codat_lending.models.shared.dataintegritydetails', 'DataIntegrityDetailsTypedDict'),
    'DataIntegrityMatch': ('codat_lending.models.shared.dataintegritymatch', 'DataIntegrityMatch'),
    'DataIntegrityMatchTypedDict': ('codat_lending.models.shared.dataintegritymatch', 'DataIntegrityMatchTypedDict'),
    'DataIntegrityStatus': ('codat_lending.models.shared.dataintegritystatus', 'DataIntegrityStatus'),
    'DataIntegrityStatusInfo': ('codat_lending.models.shared.dataintegritystatusinfo', 'DataIntegrityStatusInfo'),
    'DataIntegrityStatusInfoTypedDict': ('codat_lending.models.shared.dataintegritystatusinfo', 'DataIntegrityStatusInfoTypedDict'),
    'DataIntegrityStatusTypedDict': ('codat_lending.models.shared.dataintegritystatus', 'DataIntegrityStatusTypedDict'),
    'DataIntegrityStatuses': ('codat_lending.models.shared.dataintegritystatuses', 'DataIntegrityStatuses'),
    'DataIntegrityStatusesTypedDict': ('codat_lending.models.shared.dataintegritystatuses', 'DataIntegrityStatusesTypedDict'),
    'DataIntegritySummaries': ('codat_lending.models.shared.dataintegritysummaries', 'DataIntegritySummaries'),
    'DataIntegritySummariesTypedDict': ('codat_lending.models.shared.dataintegritysummaries', 'DataIntegritySummariesTypedDict'),
    'DataIntegritySummary': ('codat_lending.models.shared.dataintegritysummary', 'DataIntegritySummary'),
    'DataIntegritySummaryTypedDict': ('codat_lending.models.shared.dataintegritysummary', 'DataIntegritySummaryTypedDict'),
    'DataIntegrityType': ('codat_lending.models.data_integrity_type', 'DataIntegrityType'),
    'DataIntegrityTypeTypedDict': ('codat_lending.models.data_integrity_type', 'DataIntegrityTypeTypedDict'),
    'DataSource': ('codat_lending.models.shared.datasource', 'DataSource'),
    'DataSourceTypedDict': ('codat_lending.models.shared.datasource', 'DataSourceTypedDict'),
    'DataStatus': ('codat_lending.models.shared.datastatus', 'DataStatus'),
    'DataStatusTypedDict': ('codat_lending.models.shared.datastatus', 'DataStatusTypedDict'),
    'DataStatuses': ('codat_lending.models.data_statuses', 'DataStatuses'),
    'DataStatusesTypedDict': ('codat_lending.models.data_statuses', 'DataStatusesTypedDict'),
    'DataType': ('codat_lending.models.shared.datatype', 'DataType'),
    'DataTypes': ('codat_lending.models.data_types', 'DataTypes'),
    'DatasetStatus': ('codat_lending.models.dataset_status', 'DatasetStatus'),
    'DirectCostLineItem': ('codat_lending.models.shared.directcostlineitem', 'DirectCostLineItem'),
    'DirectCostLineItemTypedDict': ('codat_lending.models.shared.directcostlineitem', 'DirectCostLineItemTypedDict'),
    'DirectCostPrototype': ('codat_lending.models.shared.directcostprototype', 'DirectCostPrototype'),
    'DirectCostPrototypeTypedDict': ('codat_lending.models.shared.directcostprototype', 'DirectCostPrototypeTypedDict'),
    'DirectIncomeLineItem': ('codat_lending.models.shared.directincomelineitem', 'DirectIncomeLineItem'),
    'DirectIncomeLineItemTypedDict': ('codat_lending.models.shared.directincomelineitem', 'DirectIncomeLineItemTypedDict'),
    'DisputeStatus': ('codat_lending.models.shared.disputestatus', 'DisputeStatus'),
    'EndUploadSessionRequest': ('codat_lending.models.shared.enduploadsessionrequest', 'EndUploadSessionRequest'),
    'EndUploadSessionRequestStatus': ('codat_lending.models.end_upload_session_request_status', 'EndUploadSessionRequestStatus'),
    'EndUploadSessionRequestTypedDict': ('codat_lending.models.shared.enduploadsessionrequest', 'EndUploadSessionRequestTypedDict'),
    'EnhancedCashFlowItem': ('codat_lending.models.shared.enhancedcashflowitem', 'EnhancedCashFlowItem'),
    'EnhancedCashFlowItemTypedDict': ('codat_lending.models.shared.enhancedcashflowitem', 'EnhancedCashFlowItemTypedDict'),
    'EnhancedCashFlowTransactions': ('codat_lending.models.shared.enhancedcashflowtransactions', 'EnhancedCashFlowTransactions'),
    'EnhancedCashFlowTransactionsTypedDict': ('codat_lending.models.shared.enhancedcashflowtransactions', 'EnhancedCashFlowTransactionsTypedDict'),
    'EnhancedFinancialReport': ('codat_lending.models.shared.enhancedfinancialreport', 'EnhancedFinancialReport'),
    'EnhancedFinancialReportTypedDict': ('codat_lending.models.shared.enhancedfinancialreport', 'EnhancedFinancialReportTypedDict'),
    'EnhancedInvoiceReportItem': ('codat_lending.models.shared.enhancedinvoicereportitem', 'EnhancedInvoiceReportItem'),
    'EnhancedInvoiceReportItemTypedDict': ('codat_lending.models.shared.enhancedinvoicereportitem', 'EnhancedInvoiceReportItemTypedDict'),
    'EnhancedInvoicesReport': ('codat_lending.models.shared.enhancedinvoicesreport', 'EnhancedInvoicesReport'),
    'EnhancedInvoicesReportTypedDict': ('codat_lending.models.shared.enhancedinvoicesreport', 'EnhancedInvoicesReportTypedDict'),
    'EnhancedReportAccountCategory': ('codat_lending.models.shared.enhancedreportaccountcategory', 'EnhancedReportAccountCategory'),
    'EnhancedReportAccountCategoryTypedDict': ('codat_lending.models.shared.enhancedreportaccountcategory', 'EnhancedReportAccountCategoryTypedDict'),
    'EnhancedReportInfo': ('codat_lending.models.shared.enhancedreportinfo', 'EnhancedReportInfo'),
    'EnhancedReportInfoTypedDict': ('codat_lending.models.shared.enhancedreportinfo', 'EnhancedReportInfoTypedDict'),
    'ErrorMessage': ('codat_lending.models.error_message', 'ErrorMessage'),
    'ErrorMessageTypedDict': ('codat_lending.models.error_message', 'ErrorMessageTypedDict'),
    'ErrorStatus': ('codat_lending.models.error_status', 'ErrorStatus'),
    'ErrorValidation': ('codat_lending.models.shared.errorvalidation', 'ErrorValidation'),
    'ErrorValidationItem': ('codat_lending.models.shared.errorvalidationitem', 'ErrorValidationItem'),
    'ErrorValidationItemTypedDict': ('codat_lending.models.shared.errorvalidationitem', 'ErrorValidationItemTypedDict'),
    'ErrorValidationTypedDict': ('codat_lending.models.shared.errorvalidation', 'ErrorValidationTypedDict'),
    'ExcelReportTypes': ('codat_lending.models.shared.excelreporttypes', 'ExcelReportTypes'),
    'ExcelStatus': ('codat_lending.models.shared.excelstatus', 'ExcelStatus'),
    'ExcelStatusTypedDict': ('codat_lending.models.shared.excelstatus', 'ExcelStatusTypedDict'),
    'File': ('codat_lending.models.shared.file', 'File'),
    'FileTypedDict': ('codat_lending.models.shared.file', 'FileTypedDict'),
    'FileUpload': ('codat_lending.models.shared.fileupload', 'FileUpload'),
    'FileUploadTypedDict': ('codat_lending.models.shared.fileupload', 'FileUploadTypedDict'),
    'FinancialSummary': ('codat_lending.models.financial_summary', 'FinancialSummary'),
    'FinancialSummaryAccountingScore': ('codat_lending.models.financial_summary_accounting_score', 'FinancialSummaryAccountingScore'),
    'FinancialSummaryAccountingScoreTypedDict': ('codat_lending.models.financial_summary_accounting_score', 'FinancialSummaryAccountingScoreTypedDict'),
    'FinancialSummaryBooksClosedDate': ('codat_lending.models.financial_summary_books_closed_date', 'FinancialSummaryBooksClosedDate'),
    'FinancialSummaryBooksClosedDateTypedDict': ('codat_lending.models.financial_summary_books_closed_date', 'FinancialSummaryBooksClosedDateTypedDict'),
    'FinancialSummaryTypedDict': ('codat_lending.models.financial_summary', 'FinancialSummaryTypedDict'),
    'GetReportStatusReportIdParameter': ('codat_lending.models.get_report_status_report_id_parameter', 'GetReportStatusReportIdParameter'),
    'GetReportStatusReportIdParameterTypedDict': ('codat_lending.models.get_report_status_report_id_parameter', 'GetReportStatusReportIdParameterTypedDict'),
    'HalRef': ('codat_lending.models.shared.halref', 'HalRef'),
    'HalRefTypedDict': ('codat_lending.models.shared.halref', 'HalRefTypedDict'),
    'IntegrityStatus': ('codat_lending.models.shared.integritystatus', 'IntegrityStatus'),
    'InvoiceLineItem': ('codat_lending.models.shared.invoicelineitem', 'InvoiceLineItem'),
    'InvoiceLineItemTypedDict': ('codat_lending.models.shared.invoicelineitem', 'InvoiceLineItemTypedDict'),
    'InvoiceStatus': ('codat_lending.models.shared.invoicestatus', 'InvoiceStatus'),
    'ItemRef': ('codat_lending.models.shared.itemref', 'ItemRef'),
    'ItemRefTypedDict': ('codat_lending.models.shared.itemref', 'ItemRefTypedDict'),
    'ItemReference': ('codat_lending.models.item_reference', 'ItemReference'),
    'ItemReferenceTypedDict': ('codat_lending.models.item_reference', 'ItemReferenceTypedDict'),
    'Items': ('codat_lending.models.shared.items', 'Items'),
    'ItemsTypedDict': ('codat_lending.models.shared.items', 'ItemsTypedDict'),
    'JournalEntryRecordRef': ('codat_lending.models.shared.journalentryrecordref', 'JournalEntryRecordRef'),
    'JournalEntryRecordRefDataType': ('codat_lending.models.journal_entry_record_ref_data_type', 'JournalEntryRecordRefDataType'),
    'JournalEntryRecordRefTypedDict': ('codat_lending.models.shared.journalentryrecordref', 'JournalEntryRecordRefTypedDict'),
    'JournalLine': ('codat_lending.models.journal_line', 'JournalLine'),
    'JournalLineDataType': ('codat_lending.models.shared.journalline', 'JournalLineDataType'),
    'JournalLineTracking': ('codat_lending.models.journal_line_tracking', 'JournalLineTracking'),
    'JournalLineTrackingDataType': ('codat_lending.models.journal_line_tracking_data_type', 'JournalLineTrackingDataType'),
    'JournalLineTrackingTypedDict': ('codat_lending.models.journal_line_tracking', 'JournalLineTrackingTypedDict'),
    'JournalLineTypedDict': ('codat_lending.models.journal_line', 'JournalLineTypedDict'),
    'JournalPrototype': ('codat_lending.models.journal_prototype', 'JournalPrototype'),
    'JournalPrototypeTypedDict': ('codat_lending.models.journal_prototype', 'JournalPrototypeTypedDict'),
    'JournalRef': ('codat_lending.models.shared.journalref', 'JournalRef'),
    'JournalRefTypedDict': ('codat_lending.models.shared.journalref', 'JournalRefTypedDict'),
    'JournalStatus': ('codat_lending.models.shared.journalstatus', 'JournalStatus'),
    'LendingCustomerRef': ('codat_lending.models.shared.lendingcustomerref', 'LendingCustomerRef'),
    'LendingCustomerRefTypedDict': ('codat_lending.models.shared.lendingcustomerref', 'LendingCustomerRefTypedDict'),
    'Links': ('codat_lending.models.shared.links', 'Links'),
    'LinksTypedDict': ('codat_lending.models.shared.links', 'LinksTypedDict'),
    'LoanRef': ('codat_lending.models.shared.loanref', 'LoanRef'),
    'LoanRefTypedDict': ('codat_lending.models.shared.loanref', 'LoanRefTypedDict'),
    'LoanSummary': ('codat_lending.models.shared.loansummary', 'LoanSummary'),
    'LoanSummaryIntegrationType': ('codat_lending.models.shared.loansummaryintegrationtype', 'LoanSummaryIntegrationType'),
    'LoanSummaryRecordRef': ('codat_lending.models.shared.loansummaryrecordref', 'LoanSummaryRecordRef'),
    'LoanSummaryRecordRefType': ('codat_lending.models.shared.loansummaryrecordreftype', 'LoanSummaryRecordRefType'),
    'LoanSummaryRecordRefTypedDict': ('codat_lending.models.shared.loansummaryrecordref', 'LoanSummaryRecordRefTypedDict'),
    'LoanSummaryReportInfo': ('codat_lending.models.shared.loansummaryreportinfo', 'LoanSummaryReportInfo'),
    'LoanSummaryReportInfoTypedDict': ('codat_lending.models.shared.loansummaryreportinfo', 'LoanSummaryReportInfoTypedDict'),
    'LoanSummaryReportItem': ('codat_lending.models.shared.loansummaryreportitem', 'LoanSummaryReportItem'),
    'LoanSummaryReportItemTypedDict': ('codat_lending.models.shared.loansummaryreportitem', 'LoanSummaryReportItemTypedDict'),
    'LoanSummaryTypedDict': ('codat_lending.models.shared.loansummary', 'LoanSummaryTypedDict'),
    'LoanTransactionType': ('codat_lending.models.loan_transaction_type', 'LoanTransactionType'),
    'LoanTransactions': ('codat_lending.models.shared.loantransactions', 'LoanTransactions'),
    'LoanTransactionsReportInfo': ('codat_lending.models.shared.loantransactionsreportinfo', 'LoanTransactionsReportInfo'),
    'LoanTransactionsReportInfoTypedDict': ('codat_lending.models.shared.loantransactionsreportinfo', 'LoanTransactionsReportInfoTypedDict'),
    'LoanTransactionsTypedDict': ('codat_lending.models.shared.loantransactions', 'LoanTransactionsTypedDict'),
    'LocationRef': ('codat_lending.models.shared.locationref', 'LocationRef'),
    'LocationRefTypedDict': ('codat_lending.models.shared.locationref', 'LocationRefTypedDict'),
    'Metadata': ('codat_lending.models.shared.metadata', 'Metadata'),
    'MetadataTypedDict': ('codat_lending.models.shared.metadata', 'MetadataTypedDict'),
    'Model0': ('codat_lending.models.model0', 'Model0'),
    'Model0TypedDict': ('codat_lending.models.model0', 'Model0TypedDict'),
    'Model3': ('codat_lending.models.model3', 'Model3'),
    'Model3TypedDict': ('codat_lending.models.model3', 'Model3TypedDict'),
    'OrderDiscountAllocation': ('codat_lending.models.shared.orderdiscountallocation', 'OrderDiscountAllocation'),
    'OrderDiscountAllocationTypedDict': ('codat_lending.models.shared.orderdiscountallocation', 'OrderDiscountAllocationTypedDict'),
    'OrderLineItem': ('codat_lending.models.shared.orderlineitem', 'OrderLineItem'),
    'OrderLineItemTypedDict': ('codat_lending.models.shared.orderlineitem', 'OrderLineItemTypedDict'),
    'PagingInfo': ('codat_lending.models.paging_info', 'PagingInfo'),
    'PagingInfoTypedDict': ('codat_lending.models.paging_info', 'PagingInfoTypedDict'),
    'Path': ('codat_lending.models.shared.path', 'Path'),
    'Payment': ('codat_lending.models.shared.payment', 'Payment'),
    'PaymentAllocationPayment': ('codat_lending.models.shared.paymentallocationpayment', 'PaymentAllocationPayment'),
    'PaymentAllocationPaymentTypedDict': ('codat_lending.models.shared.paymentallocationpayment', 'PaymentAllocationPaymentTypedDict'),
    'PaymentLine': ('codat_lending.models.shared.paymentline', 'PaymentLine'),
    'PaymentLineLink': ('codat_lending.models.shared.paymentlinelink', 'PaymentLineLink'),
    'PaymentLineLinkTypedDict': ('codat_lending.models.shared.paymentlinelink', 'PaymentLineLinkTypedDict'),
    'PaymentLineTypedDict': ('codat_lending.models.shared.paymentline', 'PaymentLineTypedDict'),
    'PaymentLinkType': ('codat_lending.models.shared.paymentlinktype', 'PaymentLinkType'),
    'PaymentMethodRef': ('codat_lending.models.shared.paymentmethodref', 'PaymentMethodRef'),
    'PaymentMethodRefTypedDict': ('codat_lending.models.shared.paymentmethodref', 'PaymentMethodRefTypedDict'),
    'PaymentMethodType': ('codat_lending.models.payment_method_type', 'PaymentMethodType'),
    'PaymentRef': ('codat_lending.models.shared.paymentref', 'PaymentRef'),
    'PaymentRefTypedDict': ('codat_lending.models.shared.paymentref', 'PaymentRefTypedDict'),
    'PaymentStatus': ('codat_lending.models.shared.paymentstatus', 'PaymentStatus'),
    'PaymentType': ('codat_lending.models.shared.paymenttype', 'PaymentType'),
    'PaymentTypedDict': ('codat_lending.models.shared.payment', 'PaymentTypedDict'),
    'PeriodUnit': ('codat_lending.models.shared.periodunit', 'PeriodUnit'),
    'PhoneNumber': ('codat_lending.models.phone_number', 'PhoneNumber'),
    'PhoneNumberType': ('codat_lending.models.shared.phonenumber', 'PhoneNumberType'),
    'PhoneNumberTypedDict': ('codat_lending.models.phone_number', 'PhoneNumberTypedDict'),
    'ProductInventory': ('codat_lending.models.shared.productinventory', 'ProductInventory'),
    'ProductInventoryLocation': ('codat_lending.models.shared.productinventorylocation', 'ProductInventoryLocation'),
    'ProductInventoryLocationTypedDict': ('codat_lending.models.shared.productinventorylocation', 'ProductInventoryLocationTypedDict'),
    'ProductInventoryTypedDict': ('codat_lending.models.shared.productinventory', 'ProductInventoryTypedDict'),
    'ProductPrice': ('codat_lending.models.shared.productprice', 'ProductPrice'),
    'ProductPriceTypedDict': ('codat_lending.models.shared.productprice', 'ProductPriceTypedDict'),
    'ProductRef': ('codat_lending.models.shared.productref', 'ProductRef'),
    'ProductRefTypedDict': ('codat_lending.models.shared.productref', 'ProductRefTypedDict'),
    'ProductVariant': ('codat_lending.models.shared.productvariant', 'ProductVariant'),
    'ProductVariantRef': ('codat_lending.models.shared.productvariantref', 'ProductVariantRef'),
    'ProductVariantRefTypedDict': ('codat_lending.models.shared.productvariantref', 'ProductVariantRefTypedDict'),
    'ProductVariantStatus': ('codat_lending.models.shared.productvariantstatus', 'ProductVariantStatus'),
    'ProductVariantTypedDict': ('codat_lending.models.shared.productvariant', 'ProductVariantTypedDict'),
    'ProfitAndLossReport': ('codat_lending.models.shared.profitandlossreport', 'ProfitAndLossReport'),
    'ProfitAndLossReportTypedDict': ('codat_lending.models.shared.profitandlossreport', 'ProfitAndLossReportTypedDict'),
    'ProjectRef': ('codat_lending.models.shared.projectref', 'ProjectRef'),
    'ProjectRefTypedDict': ('codat_lending.models.shared.projectref', 'ProjectRefTypedDict'),
    'PropertieAccountType': ('codat_lending.models.shared.propertie_accounttype', 'PropertieAccountType'),
    'PropertieItemRef': ('codat_lending.models.item_reference', 'ItemReference'),
    'PropertieItemRefTypedDict': ('codat_lending.models.item_reference', 'ItemReferenceTypedDict'),
    'PullOperation': ('codat_lending.models.shared.pulloperation', 'PullOperation'),
    'PullOperationTypedDict': ('codat_lending.models.shared.pulloperation', 'PullOperationTypedDict'),
    'PullOperations': ('codat_lending.models.shared.pulloperations', 'PullOperations'),
    'PullOperationsTypedDict': ('codat_lending.models.shared.pulloperations', 'PullOperationsTypedDict'),
    'PurchaseOrderReference': ('codat_lending.models.purchase_order_reference', 'PurchaseOrderReference'),
    'PurchaseOrderReferenceTypedDict': ('codat_lending.models.purchase_order_reference', 'PurchaseOrderReferenceTypedDict'),
    'PushChangeType': ('codat_lending.models.shared.pushchangetype', 'PushChangeType'),
    'PushFieldValidation': ('codat_lending.models.shared.pushfieldvalidation', 'PushFieldValidation'),
    'PushFieldValidationTypedDict': ('codat_lending.models.shared.pushfieldvalidation', 'PushFieldValidationTypedDict'),
    'PushOperation': ('codat_lending.models.shared.pushoperation', 'PushOperation'),
    'PushOperationChange': ('codat_lending.models.shared.pushoperationchange', 'PushOperationChange'),
    'PushOperationChangeTypedDict': ('codat_lending.models.shared.pushoperationchange', 'PushOperationChangeTypedDict'),
    'PushOperationRef': ('codat_lending.models.shared.pushoperationref', 'PushOperationRef'),
    'PushOperationRefTypedDict': ('codat_lending.models.shared.pushoperationref', 'PushOperationRefTypedDict'),
    'PushOperationStatus': ('codat_lending.models.shared.pushoperationstatus', 'PushOperationStatus'),
    'PushOperationTypedDict': ('codat_lending.models.shared.pushoperation', 'PushOperationTypedDict'),
    'PushOperations': ('codat_lending.models.shared.pushoperations', 'PushOperations'),
    'PushOperationsTypedDict': ('codat_lending.models.shared.pushoperations', 'PushOperationsTypedDict'),
    'PushOption': ('codat_lending.models.shared.pushoption', 'PushOption'),
    'PushOptionChoice': ('codat_lending.models.shared.pushoptionchoice', 'PushOptionChoice'),
    'PushOptionChoiceTypedDict': ('codat_lending.models.shared.pushoptionchoice', 'PushOptionChoiceTypedDict'),
    'PushOptionProperty': ('codat_lending.models.shared.pushoptionproperty', 'PushOptionProperty'),
    'PushOptionPropertyTypedDict': ('codat_lending.models.shared.pushoptionproperty', 'PushOptionPropertyTypedDict'),
    'PushOptionType': ('codat_lending.models.shared.pushoptiontype', 'PushOptionType'),
    'PushOptionTypedDict': ('codat_lending.models.shared.pushoption', 'PushOptionTypedDict'),
    'PushValidationInfo': ('codat_lending.models.shared.pushvalidationinfo', 'PushValidationInfo'),
    'PushValidationInfoTypedDict': ('codat_lending.models.shared.pushvalidationinfo', 'PushValidationInfoTypedDict'),
    'RecordLineReference': ('codat_lending.models.record_line_reference', 'RecordLineReference'),
    'RecordLineReferenceDataType': ('codat_lending.models.record_line_reference_data_type', 'RecordLineReferenceDataType'),
    'RecordLineReferenceTypedDict': ('codat_lending.models.record_line_reference', 'RecordLineReferenceTypedDict'),
    'ReportBasis': ('codat_lending.models.shared.reportbasis', 'ReportBasis'),
    'ReportComponentMeasure': ('codat_lending.models.shared.reportcomponentmeasure', 'ReportComponentMeasure'),
    'ReportComponentMeasureTypedDict': ('codat_lending.models.shared.reportcomponentmeasure', 'ReportComponentMeasureTypedDict'),
    'ReportGenerationPayload': ('codat_lending.models.shared.reportgenerationpayload', 'ReportGenerationPayload'),
    'ReportGenerationPayloadTypedDict': ('codat_lending.models.shared.reportgenerationpayload', 'ReportGenerationPayloadTypedDict'),
    'ReportInfo': ('codat_lending.models.shared.reportinfo', 'ReportInfo'),
    'ReportInfoTypedDict': ('codat_lending.models.shared.reportinfo', 'ReportInfoTypedDict'),
    'ReportInput': ('codat_lending.models.shared.reportinput', 'ReportInput'),
    'ReportItem': ('codat_lending.models.report_item', 'ReportItem'),
    'ReportItemTypedDict': ('codat_lending.models.report_item', 'ReportItemTypedDict'),
    'ReportItems': ('codat_lending.models.shared.reportitems', 'ReportItems'),
    'ReportItemsTypedDict': ('codat_lending.models.shared.reportitems', 'ReportItemsTypedDict'),
    'ReportLine': ('codat_lending.models.shared.reportline', 'ReportLine'),
    'ReportLineTypedDict': ('codat_lending.models.shared.reportline', 'ReportLineTypedDict'),
    'ReportOperation': ('codat_lending.models.shared.reportoperation', 'ReportOperation'),
    'ReportOperationStatus': ('codat_lending.models.report_operation_status', 'ReportOperationStatus'),
    'ReportOperationType': ('codat_lending.models.report_operation_type', 'ReportOperationType'),
    'ReportOperationTypedDict': ('codat_lending.models.shared.reportoperation', 'ReportOperationTypedDict'),
    'ReportSourceReference': ('codat_lending.models.report_source_reference', 'ReportSourceReference'),
    'ReportSourceReferenceTypedDict': ('codat_lending.models.report_source_reference', 'ReportSourceReferenceTypedDict'),
    'ReportType': ('codat_lending.models.shared.reporttype', 'ReportType'),
    'Reports': ('codat_lending.models.shared.reports', 'Reports'),
    'ReportsTypedDict': ('codat_lending.models.shared.reports', 'ReportsTypedDict'),
    'RoutingInfo': ('codat_lending.models.shared.routinginfo', 'RoutingInfo'),
    'RoutingInfoTypedDict': ('codat_lending.models.shared.routinginfo', 'RoutingInfoTypedDict'),
    'SalesOrderReference': ('codat_lending.models.sales_order_reference', 'SalesOrderReference'),
    'SalesOrderReferenceTypedDict': ('codat_lending.models.sales_order_reference', 'SalesOrderReferenceTypedDict'),
    'Schema': ('codat_lending.models.shared.schema', 'Schema'),
    'SchemaDataType': ('codat_lending.models.shared.schema_datatype', 'SchemaDataType'),
    'SchemaTypedDict': ('codat_lending.models.shared.schema', 'SchemaTypedDict'),
    'Security': ('codat_lending.models.shared.security', 'Security'),
    'SecurityTypedDict': ('codat_lending.models.shared.security', 'SecurityTypedDict'),
    'ServiceCharge': ('codat_lending.models.shared.servicecharge', 'ServiceCharge'),
    'ServiceChargeType': ('codat_lending.models.shared.servicechargetype', 'ServiceChargeType'),
    'ServiceChargeTypedDict': ('codat_lending.models.shared.servicecharge', 'ServiceChargeTypedDict'),
    'Source': ('codat_lending.models.source', 'Source'),
    'SourceAccount': ('codat_lending.models.shared.sourceaccount', 'SourceAccount'),
    'SourceAccountPrototype': ('codat_lending.models.shared.sourceaccountprototype', 'SourceAccountPrototype'),
    'SourceAccountPrototypeTypedDict': ('codat_lending.models.shared.sourceaccountprototype', 'SourceAccountPrototypeTypedDict'),
    'SourceAccountStatus': ('codat_lending.models.source_account_status', 'SourceAccountStatus'),
    'SourceAccountTypedDict': ('codat_lending.models.shared.sourceaccount', 'SourceAccountTypedDict'),
    'SourceAccountV2': ('codat_lending.models.source_account_v2', 'SourceAccountV2'),
    'SourceAccountV2AccountType': ('codat_lending.models.shared.sourceaccountv2', 'SourceAccountV2AccountType'),
    'SourceAccountV2Prototype': ('codat_lending.models.shared.sourceaccountv2prototype', 'SourceAccountV2Prototype'),
    'SourceAccountV2PrototypeTypedDict': ('codat_lending.models.shared.sourceaccountv2prototype', 'SourceAccountV2PrototypeTypedDict'),
    'SourceAccountV2Status': ('codat_lending.models.source_account_v2_status', 'SourceAccountV2Status'),
    'SourceAccountV2Type': ('codat_lending.models.source_account_v2_type', 'SourceAccountV2Type'),
    'SourceAccountV2TypedDict': ('codat_lending.models.source_account_v2', 'SourceAccountV2TypedDict'),
    'SourceRef': ('codat_lending.models.shared.sourceref', 'SourceRef'),
    'SourceRefTypedDict': ('codat_lending.models.shared.sourceref', 'SourceRefTypedDict'),
    'SourceType': ('codat_lending.models.source_type', 'SourceType'),
    'StartUploadSessionRequest': ('codat_lending.models.shared.startuploadsessionrequest', 'StartUploadSessionRequest'),
    'StartUploadSessionRequestDataType': ('codat_lending.models.start_upload_session_request_data_type', 'StartUploadSessionRequestDataType'),
    'StartUploadSessionRequestTypedDict': ('codat_lending.models.shared.startuploadsessionrequest', 'StartUploadSessionRequestTypedDict'),
    'Status': ('codat_lending.models.shared.status', 'Status'),
    'SupplementalData': ('codat_lending.models.shared.supplementaldata', 'SupplementalData'),
    'SupplementalDataTypedDict': ('codat_lending.models.shared.supplementaldata', 'SupplementalDataTypedDict'),
    'SupplierRef': ('codat_lending.models.shared.supplierref', 'SupplierRef'),
    'SupplierRefTypedDict': ('codat_lending.models.shared.supplierref', 'SupplierRefTypedDict'),
    'SupplierStatus': ('codat_lending.models.shared.supplierstatus', 'SupplierStatus'),
    'TargetAccountOption': ('codat_lending.models.shared.targetaccountoption', 'TargetAccountOption'),
    'TargetAccountOptionTypedDict': ('codat_lending.models.shared.targetaccountoption', 'TargetAccountOptionTypedDict'),
    'TaxComponentAllocation': ('codat_lending.models.shared.taxcomponentallocation', 'TaxComponentAllocation'),
    'TaxComponentAllocationTypedDict': ('codat_lending.models.shared.taxcomponentallocation', 'TaxComponentAllocationTypedDict'),
    'TaxComponentRef': ('codat_lending.models.shared.taxcomponentref', 'TaxComponentRef'),
    'TaxComponentRefTypedDict': ('codat_lending.models.shared.taxcomponentref', 'TaxComponentRefTypedDict'),
    'TaxRateRef': ('codat_lending.models.shared.taxrateref', 'TaxRateRef'),
    'TaxRateRefTypedDict': ('codat_lending.models.shared.taxrateref', 'TaxRateRefTypedDict'),
    'TaxRateReference': ('codat_lending.models.tax_rate_reference', 'TaxRateReference'),
    'TaxRateReferenceTypedDict': ('codat_lending.models.tax_rate_reference', 'TaxRateReferenceTypedDict'),
    'Tracking': ('codat_lending.models.shared.tracking', 'Tracking'),
    'TrackingCategoryRef': ('codat_lending.models.shared.trackingcategoryref', 'TrackingCategoryRef'),
    'TrackingCategoryRefTypedDict': ('codat_lending.models.shared.trackingcategoryref', 'TrackingCategoryRefTypedDict'),
    'TrackingRecordRef': ('codat_lending.models.tracking_record_ref', 'TrackingRecordRef'),
    'TrackingRecordRefDataType': ('codat_lending.models.shared.trackingrecordref', 'TrackingRecordRefDataType'),
    'TrackingRecordRefTypedDict': ('codat_lending.models.tracking_record_ref', 'TrackingRecordRefTypedDict'),
    'TrackingTypedDict': ('codat_lending.models.shared.tracking', 'TrackingTypedDict'),
    'TransactionCategory': ('codat_lending.models.shared.transactioncategory', 'TransactionCategory'),
    'TransactionCategoryRef': ('codat_lending.models.shared.transactioncategoryref', 'TransactionCategoryRef'),
    'TransactionCategoryRefTypedDict': ('codat_lending.models.shared.transactioncategoryref', 'TransactionCategoryRefTypedDict'),
    'TransactionCategoryStatus': ('codat_lending.models.shared.transactioncategorystatus', 'TransactionCategoryStatus'),
    'TransactionCategoryTypedDict': ('codat_lending.models.shared.transactioncategory', 'TransactionCategoryTypedDict'),
    'TransactionCode': ('codat_lending.models.shared.transactioncode', 'TransactionCode'),
    'TransactionSourceRef': ('codat_lending.models.shared.transactionsourceref', 'TransactionSourceRef'),
    'TransactionSourceRefTypedDict': ('codat_lending.models.shared.transactionsourceref', 'TransactionSourceRefTypedDict'),
    'TransactionSourceType': ('codat_lending.models.shared.transactionsourcetype', 'TransactionSourceType'),
    'TransactionType': ('codat_lending.models.shared.transactiontype', 'TransactionType'),
    'TransferAccount': ('codat_lending.models.shared.transferaccount', 'TransferAccount'),
    'TransferAccountTypedDict': ('codat_lending.models.shared.transferaccount', 'TransferAccountTypedDict'),
    'Type': ('codat_lending.models.type', 'Type'),
    'UpdateConnection': ('codat_lending.models.update_connection', 'UpdateConnection'),
    'UpdateConnectionTypedDict': ('codat_lending.models.update_connection', 'UpdateConnectionTypedDict'),
    'UploadBankStatementDataRequest': ('codat_lending.models.upload_bank_statement_data_request', 'UploadBankStatementDataRequest'),
    'UploadBankStatementDataRequestTypedDict': ('codat_lending.models.upload_bank_statement_data_request', 'UploadBankStatementDataRequestTypedDict'),
    'ValidDataTypeLinks': ('codat_lending.models.valid_data_type_links', 'ValidDataTypeLinks'),
    'ValidDataTypeLinksTypedDict': ('codat_lending.models.valid_data_type_links', 'ValidDataTypeLinksTypedDict'),
    'Validation': ('codat_lending.models.shared.validation', 'Validation'),
    'ValidationItem': ('codat_lending.models.shared.validationitem', 'ValidationItem'),
    'ValidationItemTypedDict': ('codat_lending.models.shared.validationitem', 'ValidationItemTypedDict'),
    'ValidationTypedDict': ('codat_lending.models.shared.validation', 'ValidationTypedDict'),
    'WebLink': ('codat_lending.models.shared.weblink', 'WebLink'),
    'WebLinkType': ('codat_lending.models.web_link_type', 'WebLinkType'),
    'WebLinkTypedDict': ('codat_lending.models.shared.weblink', 'WebLinkTypedDict'),
    'WithholdingTax': ('codat_lending.models.withholding_tax', 'WithholdingTax'),
    'WithholdingTaxTypedDict': ('codat_lending.models.withholding_tax', 'WithholdingTaxTypedDict'),
    'Zero': ('codat_lending.models.record_line_reference', 'RecordLineReference'),
    'ZeroDataType': ('codat_lending.models.shared.zero', 'ZeroDataType'),
    'ZeroTypedDict': ('codat_lending.models.record_line_reference', 'RecordLineReferenceTypedDict'),
}


def __getattr__(attr_name):
    try:
        module_path, source_name = _dynamic_imports[attr_name]
    except KeyError:
        raise AttributeError(
            f"module {__name__!r} has no attribute {attr_name!r}"
        ) from None
    module = import_module(module_path, __package__)
    return getattr(module, source_name)


def __dir__():
    return sorted(set(globals()) | set(_dynamic_imports))
