"""codat_sync_for_payables.models.operations — re-exports of per-operation request envelopes."""

from codat_sync_for_payables.api.bank_accounts import (
    CreateBankAccountRequest,
    CreateBankAccountRequestTypedDict,
)
from codat_sync_for_payables.api.bill_payments import (
    CreateBillPaymentRequest,
    CreateBillPaymentRequestTypedDict,
    GetMappingOptionsPaymentsRequest,
    GetMappingOptionsPaymentsRequestTypedDict,
)
from codat_sync_for_payables.api.bills import (
    CreateBillRequest,
    CreateBillRequestTypedDict,
    DownloadBillAttachmentRequest,
    DownloadBillAttachmentRequestTypedDict,
    GetMappingOptionsBillsRequest,
    GetMappingOptionsBillsRequestTypedDict,
    ListBillAttachmentsRequest,
    ListBillAttachmentsRequestTypedDict,
    ListBillsRequest,
    ListBillsRequestTypedDict,
    UpdateBillRequest,
    UpdateBillRequestTypedDict,
    UploadBillAttachmentRequest,
    UploadBillAttachmentRequestTypedDict,
)
from codat_sync_for_payables.api.companies import (
    CreateCompanyRequest,
    CreateCompanyRequestTypedDict,
    DeleteCompanyRequest,
    DeleteCompanyRequestTypedDict,
    GetCompanyRequest,
    GetCompanyRequestTypedDict,
    ListCompaniesRequest,
    ListCompaniesRequestTypedDict,
    ReplaceCompanyRequest,
    ReplaceCompanyRequestTypedDict,
    UpdateCompanyRequest,
    UpdateCompanyRequestTypedDict,
)
from codat_sync_for_payables.api.company_information import (
    GetCompanyInformationRequest,
    GetCompanyInformationRequestTypedDict,
)
from codat_sync_for_payables.api.connections import (
    CreateConnectionRequest,
    CreateConnectionRequestTypedDict,
    DeleteConnectionRequest,
    DeleteConnectionRequestTypedDict,
    GetConnectionRequest,
    GetConnectionRequestTypedDict,
    ListConnectionsRequest,
    ListConnectionsRequestTypedDict,
    UnlinkConnectionRequest,
    UnlinkConnectionRequestTypedDict,
)
from codat_sync_for_payables.api.suppliers import (
    CreateSupplierRequest,
    CreateSupplierRequestTypedDict,
    ListSuppliersRequest,
    ListSuppliersRequestTypedDict,
    UpdateSupplierRequest,
    UpdateSupplierRequestTypedDict,
)

# Speakeasy request-body class names (aliases to POC body classes).
from codat_sync_for_payables.models.create_connection_request import CreateConnectionRequest as CreateConnectionRequestBody
from codat_sync_for_payables.models.update_connection import UpdateConnection as UnlinkConnectionUpdateConnection

# Speakeasy TypedDict companions for aliased names.
from codat_sync_for_payables.models.create_connection_request import CreateConnectionRequestTypedDict as CreateConnectionRequestBodyTypedDict
from codat_sync_for_payables.models.update_connection import UpdateConnectionTypedDict as UnlinkConnectionUpdateConnectionTypedDict
