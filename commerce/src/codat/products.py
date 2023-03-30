"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from codat.models import operations, shared
from typing import Optional

class Products:
    r"""Retrieve standardized data from linked commerce platforms."""
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
        
    def list_product_categories(self, request: operations.ListProductCategoriesRequest) -> operations.ListProductCategoriesResponse:
        r"""List product categories
        Product categories are used to classify a group of products together, either by type (eg \"Furniture\"), or sometimes by tax profile.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListProductCategoriesRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/commerce-productCategories', request)
        
        query_params = utils.get_query_params(operations.ListProductCategoriesRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListProductCategoriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ProductCategories])
                res.product_categories = out

        return res

    def list_products(self, request: operations.ListProductsRequest) -> operations.ListProductsResponse:
        r"""List products
        The Products data type provides the company's product inventory, and includes the price and quantity of all products, and product variants, available for sale.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.ListProductsRequest, base_url, '/companies/{companyId}/connections/{connectionId}/data/commerce-products', request)
        
        query_params = utils.get_query_params(operations.ListProductsRequest, request)
        
        client = self._security_client
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListProductsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Products])
                res.products = out

        return res

    