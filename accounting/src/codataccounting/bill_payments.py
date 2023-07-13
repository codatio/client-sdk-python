"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codataccounting import utils
from codataccounting.models import operations, shared
from typing import Optional

class BillPayments:
    r"""Bill payments"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create(self, request: operations.CreateBillPaymentRequest, retries: Optional[utils.RetryConfig] = None) -> operations.CreateBillPaymentResponse:
        r"""Create bill payments
        The *Create bill payment* endpoint creates a new [bill payment](https://docs.codat.io/accounting-api#/schemas/BillPayment) for a given company's connection.

        [Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

        **Integration-specific behaviour**

        Required data may vary by integration. To see what data to post, first call [Get create bill payment model](https://docs.codat.io/accounting-api#/operations/get-create-billPayments-model).

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating an account.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateBillPaymentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/billPayments', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bill_payment", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.CreateBillPaymentRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateBillPaymentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateBillPaymentResponse])
                res.create_bill_payment_response = out
        elif http_res.status_code in [400, 401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Schema])
                res.schema = out

        return res

    
    def delete(self, request: operations.DeleteBillPaymentRequest, retries: Optional[utils.RetryConfig] = None) -> operations.DeleteBillPaymentResponse:
        r"""Delete bill payment
        The *Delete bill payment* endpoint allows you to delete a specified bill payment from an accounting platform.

        [Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

        ### Process
        1. Pass the `{billPaymentId}` to the *Delete bill payment* endpoint and store the `pushOperationKey` returned.
        2. Check the status of the delete operation by checking the status of push operation either via
            1. [Push operation webhook](https://docs.codat.io/introduction/webhooks/core-rules-types#push-operation-status-has-changed) (advised),
            2. [Push operation status endpoint](https://docs.codat.io/codat-api#/operations/get-push-operation).

           A `Success` status indicates that the bill payment object was deleted from the accounting platform.
        3. (Optional) Check that the bill payment was deleted from the accounting platform.

        ### Effect on related objects
        Be aware that deleting a bill payment from an accounting platform might cause related objects to be modified.

        ## Integration specifics
        Integrations that support soft delete do not permanently delete the object in the accounting platform.

        | Integration | Soft Delete | Details                                                                                             |  
        |-------------|-------------|-----------------------------------------------------------------------------------------------------|
        | Oracle NetSuite   | No          | See [here](/integrations/accounting/netsuite/how-deleting-bill-payments-works) to learn more. |

        > **Supported Integrations**
        >
        > This functionality is currently only supported for our QuickBooks Online abd Oracle NetSuite integrations. Check out our [public roadmap](https://portal.productboard.com/codat/7-public-product-roadmap/tabs/46-accounting-api) to see what we're building next, and to submit ideas for new features.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteBillPaymentRequest, base_url, '/companies/{companyId}/connections/{connectionId}/push/billPayments/{billPaymentId}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('DELETE', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteBillPaymentResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PushOperationSummary])
                res.push_operation_summary = out
        elif http_res.status_code in [401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Schema])
                res.schema = out

        return res

    
    def get(self, request: operations.GetBillPaymentsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetBillPaymentsResponse:
        r"""Get bill payment
        The *Get bill payment* endpoint returns a single bill payment for a given billPaymentId.

        [Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support getting a specific bill payment.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetBillPaymentsRequest, base_url, '/companies/{companyId}/data/billPayments/{billPaymentId}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetBillPaymentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BillPayment])
                res.bill_payment = out
        elif http_res.status_code in [401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Schema])
                res.schema = out
        elif http_res.status_code == 409:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetBillPayments409ApplicationJSON])
                res.get_bill_payments_409_application_json_object = out

        return res

    
    def get_create_model(self, request: operations.GetCreateBillPaymentsModelRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCreateBillPaymentsModelResponse:
        r"""Get create bill payment model
        The *Get create bill payment model* endpoint returns the expected data for the request payload when creating a [bill payment](https://docs.codat.io/accounting-api#/schemas/BillPayment) for a given company and integration.

        [Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

        **Integration-specific behaviour**

        See the *response examples* for integration-specific indicative models.

        Check out our [coverage explorer](https://knowledge.codat.io/supported-features/accounting?view=tab-by-data-type&dataType=billPayments) for integrations that support creating a bill payment.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCreateBillPaymentsModelRequest, base_url, '/companies/{companyId}/connections/{connectionId}/options/billPayments', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCreateBillPaymentsModelResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PushOption])
                res.push_option = out
        elif http_res.status_code in [401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Schema])
                res.schema = out

        return res

    
    def list(self, request: operations.ListBillPaymentsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.ListBillPaymentsResponse:
        r"""List bill payments
        The *List bill payments* endpoint returns a list of [bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) for a given company's connection.

        [Bill payments](https://docs.codat.io/accounting-api#/schemas/BillPayment) are an allocation of money within any customer accounts payable account.

        Before using this endpoint, you must have [retrieved data for the company](https://docs.codat.io/codat-api#/operations/refresh-company-data).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListBillPaymentsRequest, base_url, '/companies/{companyId}/data/billPayments', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListBillPaymentsRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0.7, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListBillPaymentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BillPayments])
                res.bill_payments = out
        elif http_res.status_code in [400, 401, 404]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Schema])
                res.schema = out
        elif http_res.status_code == 409:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListBillPayments409ApplicationJSON])
                res.list_bill_payments_409_application_json_object = out

        return res

    