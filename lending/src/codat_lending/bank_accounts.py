"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from codat_lending import utils
from codat_lending._hooks import HookContext
from codat_lending.models import errors, operations, shared
from codat_lending.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Optional, Union, cast


class BankAccounts(BaseSDK):
    def create(
        self,
        *,
        request: Union[
            operations.CreateBankAccountRequest,
            operations.CreateBankAccountRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.AccountingCreateBankAccountResponse]:
        r"""Create bank account

        The *Create bank account* endpoint creates a new [bank account](https://docs.codat.io/lending-api#/schemas/BankAccount) for a given company's connection.

        [Bank accounts](https://docs.codat.io/lending-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

        **Integration-specific behaviour**

        Required data may vary by integration. To see what data to post, first call [Get create/update bank account model](https://docs.codat.io/lending-api#/operations/get-create-update-bankAccounts-model).

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating an account.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.CreateBankAccountRequest)
        request = cast(operations.CreateBankAccountRequest, request)

        req = self.build_request(
            method="POST",
            path="/companies/{companyId}/connections/{connectionId}/push/bankAccounts",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.accounting_bank_account,
                True,
                True,
                "json",
                OptionalNullable[shared.AccountingBankAccount],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="create-bank-account",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[shared.AccountingCreateBankAccountResponse]
            )
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def create_async(
        self,
        *,
        request: Union[
            operations.CreateBankAccountRequest,
            operations.CreateBankAccountRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.AccountingCreateBankAccountResponse]:
        r"""Create bank account

        The *Create bank account* endpoint creates a new [bank account](https://docs.codat.io/lending-api#/schemas/BankAccount) for a given company's connection.

        [Bank accounts](https://docs.codat.io/lending-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

        **Integration-specific behaviour**

        Required data may vary by integration. To see what data to post, first call [Get create/update bank account model](https://docs.codat.io/lending-api#/operations/get-create-update-bankAccounts-model).

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating an account.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(request, operations.CreateBankAccountRequest)
        request = cast(operations.CreateBankAccountRequest, request)

        req = self.build_request_async(
            method="POST",
            path="/companies/{companyId}/connections/{connectionId}/push/bankAccounts",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.accounting_bank_account,
                True,
                True,
                "json",
                OptionalNullable[shared.AccountingBankAccount],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="create-bank-account",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "400",
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[shared.AccountingCreateBankAccountResponse]
            )
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def get_create_update_model(
        self,
        *,
        request: Union[
            operations.GetCreateUpdateBankAccountsModelRequest,
            operations.GetCreateUpdateBankAccountsModelRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.PushOption]:
        r"""Get create/update bank account model

        The *Get create/update bank account model* endpoint returns the expected data for the request payload when creating and updating a [bank account](https://docs.codat.io/lending-api#/schemas/BankAccount) for a given company and integration.

        [Bank accounts](https://docs.codat.io/lending-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

        **Integration-specific behaviour**

        See the *response examples* for integration-specific indicative models.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating and updating a bank account.


        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, operations.GetCreateUpdateBankAccountsModelRequest
            )
        request = cast(operations.GetCreateUpdateBankAccountsModelRequest, request)

        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/options/bankAccounts",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="get-create-update-bankAccounts-model",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.PushOption])
        if utils.match_response(
            http_res,
            ["401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def get_create_update_model_async(
        self,
        *,
        request: Union[
            operations.GetCreateUpdateBankAccountsModelRequest,
            operations.GetCreateUpdateBankAccountsModelRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.PushOption]:
        r"""Get create/update bank account model

        The *Get create/update bank account model* endpoint returns the expected data for the request payload when creating and updating a [bank account](https://docs.codat.io/lending-api#/schemas/BankAccount) for a given company and integration.

        [Bank accounts](https://docs.codat.io/lending-api#/schemas/BankAccount) are financial accounts maintained by a bank or other financial institution.

        **Integration-specific behaviour**

        See the *response examples* for integration-specific indicative models.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=bankAccounts) for integrations that support creating and updating a bank account.


        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, operations.GetCreateUpdateBankAccountsModelRequest
            )
        request = cast(operations.GetCreateUpdateBankAccountsModelRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/options/bankAccounts",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config
            else:
                retries = utils.RetryConfig(
                    "backoff", utils.BackoffStrategy(500, 60000, 1.5, 3600000), True
                )

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["408", "429", "5XX"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="get-create-update-bankAccounts-model",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "401",
                "402",
                "403",
                "404",
                "429",
                "4XX",
                "500",
                "503",
                "5XX",
            ],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[shared.PushOption])
        if utils.match_response(
            http_res,
            ["401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )
