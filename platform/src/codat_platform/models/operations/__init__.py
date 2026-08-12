"""codat_platform.models.operations — re-exports of per-operation request envelopes."""

from codat_platform.api.companies import (
    AddProductRequest,
    AddProductRequestTypedDict,
    CreateCompanyRequest,
    CreateCompanyRequestTypedDict,
    DeleteCompanyRequest,
    DeleteCompanyRequestTypedDict,
    GetCompanyAccessTokenRequest,
    GetCompanyAccessTokenRequestTypedDict,
    GetCompanyRequest,
    GetCompanyRequestTypedDict,
    GetCompanySyncSettingsRequest,
    GetCompanySyncSettingsRequestTypedDict,
    ListCompaniesRequest,
    ListCompaniesRequestTypedDict,
    RefreshProductDataRequest,
    RefreshProductDataRequestTypedDict,
    RemoveProductRequest,
    RemoveProductRequestTypedDict,
    ReplaceCompanyRequest,
    ReplaceCompanyRequestTypedDict,
    SetCompanySyncSettingsRequest,
    SetCompanySyncSettingsRequestTypedDict,
    UpdateCompanyRequest,
    UpdateCompanyRequestTypedDict,
)
from codat_platform.api.connection_management import (
    GetConnectionManagementAccessTokenRequest,
    GetConnectionManagementAccessTokenRequestTypedDict,
)
from codat_platform.api.connections import (
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
    UpdateConnectionAuthorizationRequest,
    UpdateConnectionAuthorizationRequestTypedDict,
)
from codat_platform.api.cors import (
    SetConnectionManagementCorsSettingsRequest,
    SetConnectionManagementCorsSettingsRequestTypedDict,
)
from codat_platform.api.custom_data_type import (
    ConfigureCustomDataTypeRequest,
    ConfigureCustomDataTypeRequestTypedDict,
    GetCustomDataTypeConfigurationRequest,
    GetCustomDataTypeConfigurationRequestTypedDict,
    ListCustomDataTypeRecordsRequest,
    ListCustomDataTypeRecordsRequestTypedDict,
    RefreshCustomDataTypeRequest,
    RefreshCustomDataTypeRequestTypedDict,
)
from codat_platform.api.integrations import (
    GetIntegrationRequest,
    GetIntegrationRequestTypedDict,
    GetIntegrationsBrandingRequest,
    GetIntegrationsBrandingRequestTypedDict,
    ListIntegrationsRequest,
    ListIntegrationsRequestTypedDict,
)
from codat_platform.api.push_data import (
    GetCompanyPushHistoryRequest,
    GetCompanyPushHistoryRequestTypedDict,
    GetCreateUpdateModelOptionsByDataTypeRequest,
    GetCreateUpdateModelOptionsByDataTypeRequestTypedDict,
    GetPushOperationRequest,
    GetPushOperationRequestTypedDict,
)
from codat_platform.api.read_data import (
    GetReadValidationResultsRequest,
    GetReadValidationResultsRequestTypedDict,
)
from codat_platform.api.refresh_data import (
    GetCompanyDataStatusRequest,
    GetCompanyDataStatusRequestTypedDict,
    GetPullOperationRequest,
    GetPullOperationRequestTypedDict,
    ListPullOperationsRequest,
    ListPullOperationsRequestTypedDict,
    RefreshCompanyDataRequest,
    RefreshCompanyDataRequestTypedDict,
    RefreshDataTypeRequest,
    RefreshDataTypeRequestTypedDict,
)
from codat_platform.api.settings import (
    CreateAPIKeyRequest,
    CreateApiKeyRequest,
    CreateApiKeyRequestTypedDict,
    DeleteAPIKeyRequest,
    DeleteAPIKeyRequest as DeleteApiKeyRequest,
    DeleteAPIKeyRequestTypedDict,
    DeleteAPIKeyRequestTypedDict as DeleteApiKeyRequestTypedDict,
    SetCorsSettingsRequest,
    SetCorsSettingsRequestTypedDict,
    UpdateProfileRequest,
    UpdateProfileRequestTypedDict,
    UpdateProfileSyncSettingsRequest,
    UpdateProfileSyncSettingsRequestTypedDict,
)
from codat_platform.api.supplemental_data import (
    ConfigureSupplementalDataRequest,
    ConfigureSupplementalDataRequestTypedDict,
    GetSupplementalDataConfigurationRequest,
    GetSupplementalDataConfigurationRequestTypedDict,
)
from codat_platform.api.webhooks import (
    CreateWebhookConsumerRequest,
    CreateWebhookConsumerRequestTypedDict,
    DeleteWebhookConsumerRequest,
    DeleteWebhookConsumerRequestTypedDict,
)

# Speakeasy request-body class names (aliases to POC body classes).
from codat_platform.models.create_connection_request import CreateConnectionRequest as CreateConnectionRequestBody
from codat_platform.models.refresh_product_data_request import RefreshProductDataRequest as RefreshProductDataRequestBody
from codat_platform.models.set_company_sync_settings_request import SetCompanySyncSettingsRequest as SetCompanySyncSettingsRequestBody

# Speakeasy operations names POC defines elsewhere (response bodies, op-param enums).
from codat_platform.models.operations.get_supplemental_data_configuration import PathParamDataType
from codat_platform.models.update_profile_sync_settings_request import UpdateProfileSyncSettingsRequestBody
from codat_platform.api.settings import UpdateProfileSyncSettingsRequestBodyTypedDict

# Speakeasy TypedDict companions for aliased names.
from codat_platform.models.create_connection_request import CreateConnectionRequestTypedDict as CreateConnectionRequestBodyTypedDict
from codat_platform.models.refresh_product_data_request import RefreshProductDataRequestTypedDict as RefreshProductDataRequestBodyTypedDict
from codat_platform.models.set_company_sync_settings_request import SetCompanySyncSettingsRequestTypedDict as SetCompanySyncSettingsRequestBodyTypedDict
