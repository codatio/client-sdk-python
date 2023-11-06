"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from codatlending import utils
from codatlending.models import errors, operations, shared
from typing import Optional

class SalesMetrics:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_customer_retention(self, request: operations.GetCommerceCustomerRetentionMetricsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCommerceCustomerRetentionMetricsResponse:
        r"""Get customer retention metrics
        The *Get customer retention metrics* endpoint returns customer retention insights for a specific company's commerce connection over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company. 

        #### Customer retention metrics

        - __Existing customers__: the number of unique customers that have placed an order(s) in the specified period and any previous period. 
        - __New customers__: the number of unique customers that have placed an order(s) in the specified period and none in any previous period.
        - __Total customers__: the total number of existing and new customers within the specified period.
        - __Retention rate__: the ratio of existing customers within the specified period compared to the total customers at the end of the previous period represented as a percentage.
        - __Repeat rate__: the ratio of existing customers to total customers over the specified period represented as a percentage.

        Learn more about the formulas used to calculate customer retention metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        #### Response structure

        The Customer retention report's dimensions and measures are:

        | Index                       | Dimensions                 |
        |-----------------------------|----------------------------|
        | `index` = 0                 | Period                     |
        | `index` = 1                 | Customer retention metrics |

        | Index                | Measures    |
        |----------------------|------------|
        | `index` = 0          | Count      |
        | `index` = 1          | Percentage |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCommerceCustomerRetentionMetricsRequest, base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/customerRetention', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetCommerceCustomerRetentionMetricsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceCustomerRetentionMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
                res.commerce_report = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_lifetime_value(self, request: operations.GetCommerceLifetimeValueMetricsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCommerceLifetimeValueMetricsResponse:
        r"""Get lifetime value metrics
        The *Get lifetime value metrics* endpoint returns the average revenue that a specific company will generate throughout its lifespan over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company.

        Learn more about the formulas used to calculate the lifetime value metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        Refer to the [commerce reporting structure](https://docs.codat.io/lending/commerce-metrics/reporting-structure) page for more detail on commerce reports in Lending.

        #### Response structure

        The Lifetime value report's dimensions and measures are:

        | Index         | Dimensions             |
        |---------------|------------------------|
        | `index` = 0   | Period                 |
        | `index` = 1   | Lifetime value metrics |

        | Index             | Measures |
        |-------------------|---------|
        |   `index` = 1     | Value   |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCommerceLifetimeValueMetricsRequest, base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/lifetimeValue', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetCommerceLifetimeValueMetricsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceLifetimeValueMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
                res.commerce_report = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_revenue(self, request: operations.GetCommerceRevenueMetricsRequest, retries: Optional[utils.RetryConfig] = None) -> operations.GetCommerceRevenueMetricsResponse:
        r"""Get commerce revenue metrics
        The *Get revenue report* endpoint returns the revenue and revenue growth for a specific company connection over one or more periods of time.

        This detail helps you assess a merchant's health and advise them on performance improvement strategies. It also provides you with key insights you need to assess the credit risk of a company. 

        Learn more about the formulas used to calculate the revenue metrics [here](https://docs.codat.io/lending/commerce-metrics/overview#what-metrics-are-available).

        Refer to the [commerce reporting structure](https://docs.codat.io/lending/commerce-metrics/reporting-structure) page for more details on commerce reports in Lending.

        #### Response structure

        The Revenue report's dimensions and measures are:

        | Index         | Dimensions |
        |---------------|------------|
        |   `index` = 0 | Period     |
        |   `index` = 1 | Revenue    |

        | Index         | Measures                                                                                                                 |
        |---------------|--------------------------------------------------------------------------------------------------------------------------|
        | `index` = 0   | Value                                                                                                                    |
        | `index` = 1   | Percentage change, defined as the change between the current and previous periods' values and expressed as a percentage. |

        The report data then combines multiple reporting dimensions and measures and outputs the value of each combination.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetCommerceRevenueMetricsRequest, base_url, '/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/revenue', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetCommerceRevenueMetricsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 3600000), True)

        def do_request():
            return client.request('GET', url, params=query_params, headers=headers)

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '408',
            '429',
            '5XX'
        ]))
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCommerceRevenueMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CommerceReport])
                res.commerce_report = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 429, 500, 503]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorMessage])
                res.error_message = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    