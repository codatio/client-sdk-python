"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codatsyncexpenses import utils
from codatsyncexpenses.models import operations, shared
from typing import Optional

class Connections:
    r"""Create and manage partner expense connection."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_partner_expense_connection(self, request: operations.CreatePartnerExpenseConnectionRequest, retries: Optional[utils.RetryConfig] = None) -> operations.CreatePartnerExpenseConnectionResponse:
        r"""Create Partner Expense connection
        Creates a Partner Expense data connection
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreatePartnerExpenseConnectionRequest, base_url, '/companies/{companyId}/sync/expenses/connections/partnerExpense', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        retry_config = retries
        if retry_config is None:
            retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('POST', url, headers=headers)
        
        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreatePartnerExpenseConnectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DataConnection])
                res.data_connection = out
        elif http_res.status_code in [400, 401, 404, 429]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Schema])
                res.schema = out

        return res

    