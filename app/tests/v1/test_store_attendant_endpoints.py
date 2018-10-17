"""Module contains tests for store attendant

specific endpoints
"""
from flask import current_app

from . import base_test
from . import helper_functions

class TestAdminEndpoints(base_test.TestBaseClass):
    """ Class contains tests for store attendant specific endpoints """


    def test_create_sale_order(self):
        """Test POST /saleorder"""
        
        # send a dummy data response for testing
        response = self.app_test_client.post('{}/saleorder'.format(
            self.BASE_URL), json=self.SALE_ORDERS, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['sale_order']['product_name'], self.SALE_ORDERS['product_name'])
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['sale_order']['product_price'], self.SALE_ORDERS['product_price'])
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['sale_order']['quantity'], self.SALE_ORDERS['quantity'])
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['sale_order']['amount'], self.SALE_ORDERS['amount'])
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'], 'Sale record added successfully')