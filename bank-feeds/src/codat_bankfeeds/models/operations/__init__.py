"""codat_bankfeeds.models.operations — re-exports of per-operation request envelopes."""

from codat_bankfeeds.api.account_mapping import (
    CreateBankAccountMappingRequest,
    CreateBankAccountMappingRequestTypedDict,
    GetBankAccountMappingRequest,
    GetBankAccountMappingRequestTypedDict,
)
from codat_bankfeeds.api.bank_accounts import (
    CreateBankAccountRequest,
    CreateBankAccountRequestTypedDict,
    GetCreateBankAccountsModelRequest,
    GetCreateBankAccountsModelRequestTypedDict,
    ListBankAccountsRequest,
    ListBankAccountsRequestTypedDict,
)
from codat_bankfeeds.api.companies import (
    CreateCompanyRequest,
    CreateCompanyRequestTypedDict,
    DeleteCompanyRequest,
    DeleteCompanyRequestTypedDict,
    GetCompanyAccessTokenRequest,
    GetCompanyAccessTokenRequestTypedDict,
    GetCompanyRequest,
    GetCompanyRequestTypedDict,
    ListCompaniesRequest,
    ListCompaniesRequestTypedDict,
    ReplaceCompanyRequest,
    ReplaceCompanyRequestTypedDict,
    UpdateCompanyRequest,
    UpdateCompanyRequestTypedDict,
)
from codat_bankfeeds.api.company_information import (
    GetCompanyInformationRequest,
    GetCompanyInformationRequestTypedDict,
)
from codat_bankfeeds.api.connections import (
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
from codat_bankfeeds.api.managed_bank_feeds import (
    GetLatestManagedBankFeedSyncRequest,
    GetLatestManagedBankFeedSyncRequestTypedDict,
    GetManagedBankFeedSyncRequest,
    GetManagedBankFeedSyncRequestTypedDict,
    RunManagedBankFeedAdHocSyncRequest,
    RunManagedBankFeedAdHocSyncRequestTypedDict,
)
from codat_bankfeeds.api.source_accounts import (
    CreateBatchSourceAccountRequest,
    CreateBatchSourceAccountRequestTypedDict,
    CreateSourceAccountRequest,
    CreateSourceAccountRequestTypedDict,
    DeleteBankFeedCredentialsRequest,
    DeleteBankFeedCredentialsRequestTypedDict,
    DeleteSourceAccountRequest,
    DeleteSourceAccountRequestTypedDict,
    GenerateCredentialsRequest,
    GenerateCredentialsRequestTypedDict,
    GenerateOtpRequest,
    GenerateOtpRequestTypedDict,
    ListSourceAccountsRequest,
    ListSourceAccountsRequestTypedDict,
    UpdateSourceAccountRequest,
    UpdateSourceAccountRequestTypedDict,
)
from codat_bankfeeds.api.transactions import (
    CreateBankTransactionsRequest,
    CreateBankTransactionsRequestTypedDict,
    GetCreateBankTransactionsModelRequest,
    GetCreateBankTransactionsModelRequestTypedDict,
    GetCreateOperationRequest,
    GetCreateOperationRequestTypedDict,
    ListCreateOperationsRequest,
    ListCreateOperationsRequestTypedDict,
)

# Speakeasy request-body class names (aliases to POC body classes).
from codat_bankfeeds.models.create_batch_source_account_request_body import CreateBatchSourceAccountRequestBody as CreateBatchSourceAccountCreateBatchSourceAccountRequestBody
from codat_bankfeeds.models.create_connection_request import CreateConnectionRequest as CreateConnectionRequestBody
from codat_bankfeeds.models.update_connection import UpdateConnection as UnlinkConnectionUpdateConnection

# Speakeasy operations names POC defines elsewhere (response bodies, op-param enums).
from codat_bankfeeds.models.operations.create_batch_source_account_request_body import CreateBatchSourceAccountRequestBody
from codat_bankfeeds.models.operations.create_batch_source_account_request_body_typed_dict import CreateBatchSourceAccountRequestBodyTypedDict
from codat_bankfeeds.models.operations.create_batch_source_account_response_body import CreateBatchSourceAccountResponseBody
from codat_bankfeeds.models.operations.create_batch_source_account_response_body_typed_dict import CreateBatchSourceAccountResponseBodyTypedDict
from codat_bankfeeds.models.operations.create_source_account_request_body import CreateSourceAccountRequestBody
from codat_bankfeeds.models.operations.create_source_account_request_body_typed_dict import CreateSourceAccountRequestBodyTypedDict
from codat_bankfeeds.models.operations.create_source_account_response_body import CreateSourceAccountResponseBody
from codat_bankfeeds.models.operations.create_source_account_response_body_typed_dict import CreateSourceAccountResponseBodyTypedDict
from codat_bankfeeds.models.operations.list_source_accounts_response_body import ListSourceAccountsResponseBody
from codat_bankfeeds.models.operations.list_source_accounts_response_body_typed_dict import ListSourceAccountsResponseBodyTypedDict
from codat_bankfeeds.models.operations.response_body import ResponseBody
from codat_bankfeeds.models.operations.response_body_typed_dict import ResponseBodyTypedDict
from codat_bankfeeds.models.operations.create_batch_source_account_response import CreateBatchSourceAccountResponse
from codat_bankfeeds.models.operations.create_batch_source_account_response_typed_dict import CreateBatchSourceAccountResponseTypedDict

# Speakeasy TypedDict companions for aliased names.
from codat_bankfeeds.models.create_batch_source_account_request_body import CreateBatchSourceAccountRequestBodyTypedDict as CreateBatchSourceAccountCreateBatchSourceAccountRequestBodyTypedDict
from codat_bankfeeds.models.create_connection_request import CreateConnectionRequestTypedDict as CreateConnectionRequestBodyTypedDict
from codat_bankfeeds.models.update_connection import UpdateConnectionTypedDict as UnlinkConnectionUpdateConnectionTypedDict
