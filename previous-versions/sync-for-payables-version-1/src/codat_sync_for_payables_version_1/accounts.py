"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from codat_sync_for_payables_version_1 import utils
from codat_sync_for_payables_version_1._hooks import HookContext
from codat_sync_for_payables_version_1.models import errors, operations, shared
from codat_sync_for_payables_version_1.types import BaseModel, OptionalNullable, UNSET
from typing import Any, Optional, Union, cast


class Accounts(BaseSDK):
    r"""Get, create, and update Accounts."""

    def create(
        self,
        *,
        request: Union[
            operations.CreateAccountRequest, operations.CreateAccountRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CreateAccountResponse]:
        r"""Create account

        The *Create account* endpoint creates a new [account](https://docs.codat.io/sync-for-payables-api#/schemas/Account) for a given company's connection.

        [Accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) are the categories a business uses to record accounting transactions.

        **Integration-specific behaviour**

        Required data may vary by integration. To see what data to post, first call [Get create account model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-chartOfAccounts-model).

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.


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
            request = utils.unmarshal(request, operations.CreateAccountRequest)
        request = cast(operations.CreateAccountRequest, request)

        req = self.build_request(
            method="POST",
            path="/companies/{companyId}/connections/{connectionId}/push/accounts",
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
                request.account_prototype,
                False,
                True,
                "json",
                Optional[shared.AccountPrototype],
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
                operation_id="create-account",
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
                http_res.text, Optional[shared.CreateAccountResponse]
            )
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_async(
        self,
        *,
        request: Union[
            operations.CreateAccountRequest, operations.CreateAccountRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.CreateAccountResponse]:
        r"""Create account

        The *Create account* endpoint creates a new [account](https://docs.codat.io/sync-for-payables-api#/schemas/Account) for a given company's connection.

        [Accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) are the categories a business uses to record accounting transactions.

        **Integration-specific behaviour**

        Required data may vary by integration. To see what data to post, first call [Get create account model](https://docs.codat.io/sync-for-payables-api#/operations/get-create-chartOfAccounts-model).

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.


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
            request = utils.unmarshal(request, operations.CreateAccountRequest)
        request = cast(operations.CreateAccountRequest, request)

        req = self.build_request_async(
            method="POST",
            path="/companies/{companyId}/connections/{connectionId}/push/accounts",
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
                request.account_prototype,
                False,
                True,
                "json",
                Optional[shared.AccountPrototype],
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
                operation_id="create-account",
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
                http_res.text, Optional[shared.CreateAccountResponse]
            )
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get(
        self,
        *,
        request: Union[
            operations.GetAccountRequest, operations.GetAccountRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.Account]:
        r"""Get account

        The *Get account* endpoint returns a single account for a given `accountId`.

        [Accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) are the categories a business uses to record accounting transactions.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support getting a specific account.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).


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
            request = utils.unmarshal(request, operations.GetAccountRequest)
        request = cast(operations.GetAccountRequest, request)

        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/data/accounts/{accountId}",
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
                operation_id="get-account",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "401",
                "402",
                "403",
                "404",
                "409",
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
            return utils.unmarshal_json(http_res.text, Optional[shared.Account])
        if utils.match_response(
            http_res,
            ["401", "402", "403", "404", "409", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_async(
        self,
        *,
        request: Union[
            operations.GetAccountRequest, operations.GetAccountRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.Account]:
        r"""Get account

        The *Get account* endpoint returns a single account for a given `accountId`.

        [Accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) are the categories a business uses to record accounting transactions.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support getting a specific account.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).


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
            request = utils.unmarshal(request, operations.GetAccountRequest)
        request = cast(operations.GetAccountRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/companies/{companyId}/data/accounts/{accountId}",
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
                operation_id="get-account",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=[
                "401",
                "402",
                "403",
                "404",
                "409",
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
            return utils.unmarshal_json(http_res.text, Optional[shared.Account])
        if utils.match_response(
            http_res,
            ["401", "402", "403", "404", "409", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get_create_model(
        self,
        *,
        request: Union[
            operations.GetCreateAccountModelRequest,
            operations.GetCreateAccountModelRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.PushOption]:
        r"""Get create account model

        The *Get create account model* endpoint returns the expected data for the request payload when creating an [account](https://docs.codat.io/sync-for-payables-api#/schemas/Account) for a given company and integration.

        [Accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) are the categories a business uses to record accounting transactions.

        **Integration-specific behaviour**

        See the *response examples* for integration-specific indicative models.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.


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
            request = utils.unmarshal(request, operations.GetCreateAccountModelRequest)
        request = cast(operations.GetCreateAccountModelRequest, request)

        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts",
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
                operation_id="get-create-account-model",
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
            http_res_text = utils.stream_to_text(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_create_model_async(
        self,
        *,
        request: Union[
            operations.GetCreateAccountModelRequest,
            operations.GetCreateAccountModelRequestTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.PushOption]:
        r"""Get create account model

        The *Get create account model* endpoint returns the expected data for the request payload when creating an [account](https://docs.codat.io/sync-for-payables-api#/schemas/Account) for a given company and integration.

        [Accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) are the categories a business uses to record accounting transactions.

        **Integration-specific behaviour**

        See the *response examples* for integration-specific indicative models.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=chartOfAccounts) for integrations that support creating an account.


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
            request = utils.unmarshal(request, operations.GetCreateAccountModelRequest)
        request = cast(operations.GetCreateAccountModelRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/companies/{companyId}/connections/{connectionId}/options/chartOfAccounts",
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
                operation_id="get-create-account-model",
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
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def list(
        self,
        *,
        request: Union[
            operations.ListAccountsRequest, operations.ListAccountsRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.Accounts]:
        r"""List accounts

        The *List accounts* endpoint returns a list of [accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) for a given company's connection.

        [Accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) are the categories a business uses to record accounting transactions.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).

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
            request = utils.unmarshal(request, operations.ListAccountsRequest)
        request = cast(operations.ListAccountsRequest, request)

        req = self.build_request(
            method="GET",
            path="/companies/{companyId}/data/accounts",
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
                operation_id="list-accounts",
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
                "409",
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
            return utils.unmarshal_json(http_res.text, Optional[shared.Accounts])
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "409", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_async(
        self,
        *,
        request: Union[
            operations.ListAccountsRequest, operations.ListAccountsRequestTypedDict
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[shared.Accounts]:
        r"""List accounts

        The *List accounts* endpoint returns a list of [accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) for a given company's connection.

        [Accounts](https://docs.codat.io/sync-for-payables-api#/schemas/Account) are the categories a business uses to record accounting transactions.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/sync-for-payables-api#/operations/refresh-company-data).

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
            request = utils.unmarshal(request, operations.ListAccountsRequest)
        request = cast(operations.ListAccountsRequest, request)

        req = self.build_request_async(
            method="GET",
            path="/companies/{companyId}/data/accounts",
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
                operation_id="list-accounts",
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
                "409",
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
            return utils.unmarshal_json(http_res.text, Optional[shared.Accounts])
        if utils.match_response(
            http_res,
            ["400", "401", "402", "403", "404", "409", "429", "500", "503"],
            "application/json",
        ):
            data = utils.unmarshal_json(http_res.text, errors.ErrorMessageData)
            raise errors.ErrorMessage(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
