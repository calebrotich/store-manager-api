"""Module contains tests for admin

specific endpoints
"""
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