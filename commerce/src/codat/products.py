import requests as requests_http
from . import utils
from codat.models import operations
from typing import Optional

class Products:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def list_commerce_product_categories(self, request: operations.ListCommerceProductCategoriesRequest) -> operations.ListCommerceProductCategoriesResponse:
        r"""List product categories
        Product categories are used to classify a group of products together, either by type (eg \"Furniture\"), or sometimes by tax profile.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListCommerceProductCategoriesRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/commerce-productCategories', request)
        
        query_params = utils.get_query_params(operations.ListCommerceProductCategoriesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListCommerceProductCategoriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCommerceProductCategoriesLinks])
                res.links = out

        return res

    def list_commerce_products(self, request: operations.ListCommerceProductsRequest) -> operations.ListCommerceProductsResponse:
        r"""List products
        The Products data type provides the company's product inventory, and includes the price and quantity of all products, and product variants, available for sale.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListCommerceProductsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/commerce-products', request)
        
        query_params = utils.get_query_params(operations.ListCommerceProductsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListCommerceProductsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListCommerceProductsLinks])
                res.links = out

        return res

    