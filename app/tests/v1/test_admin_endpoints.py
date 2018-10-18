"""Module contains tests for admin

specific endpoints
"""

import json

from flask import current_app

from . import base_test
from . import helper_functions

class TestAdminEndpoints(base_test.TestBaseClass):
    """ Class contains tests for admin specific endpoints """


    def test_add_new_product(self):
        """Test POST /products"""
        
        # send a dummy data response for testing
        response = self.app_test_client.post('{}/products'.format(
            self.BASE_URL), json=self.PRODUCT, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['product']['product_name'], self.PRODUCT['product_name'])
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['product']['product_id'], 1)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['product']['product_price'], 55000)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['product']['category'], self.PRODUCT['category'])
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'], 'Product added successfully')


    def test_fetch_sale_orders(self):
        """Test GET /saleorder - when sale order exists"""

        self.app_test_client.post(
        '{}/saleorder'.format(self.BASE_URL), data=json.dumps(dict(
                                                                sale_order_id = 1,
                                                                product_name = "Test Product",
                                                                product_price = 20,
                                                                quantity = 1,
                                                                amount = 20
                                                                )), content_type='application/json')

        response = self.app_test_client.get(
            '{}/saleorder'.format(self.BASE_URL)
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['sale_orders'][0]['product_name'], "Test Product")
