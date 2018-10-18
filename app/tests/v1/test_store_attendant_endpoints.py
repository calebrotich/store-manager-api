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


    def test_create_sale_order_parameter_missing(self):
        """Test POST /saleorder

        with one of the required parameters missing
        """
        response = self.app_test_client.post('{}/saleorder'.format(
            self.BASE_URL), json={'product_name': 'Nyundo'}, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'], 'Bad request. Request missing a required argument')


    def test_create_sale_order_price_below_one(self):
        """Test POST /saleorder

        with the price not a valid integer
        """
        response = self.app_test_client.post('{}/saleorder'.format(
            self.BASE_URL), json={'product_name': 'Nyundo', 'product_price': -1, 'quantity': 1}, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'], 'Bad request. Price of the product should be a positive integer above 0.')


    def test_create_sale_order_invalid_product_name(self):
        """Test POST /saleorder

        with the product name not a string
        """
        response = self.app_test_client.post('{}/saleorder'.format(
            self.BASE_URL), json={'product_name': 3, 'product_price': 300, 'quantity': 1}, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'], 'Bad request. Product name should be a string')


    def test_create_sale_order_price_not_digits(self):
        """Test POST /saleorder

        with the price not a valid integer
        """
        response = self.app_test_client.post('{}/saleorder'.format(
            self.BASE_URL), json={'product_name': "Nyundo", 'product_price': "300", 'quantity': 1}, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'], 'Bad request. The product price should be digits')


    def test_create_sale_order_invalid_quantity(self):
        """Test POST /saleorder

        with the quantity not a valid integer
        """
        response = self.app_test_client.post('{}/saleorder'.format(
            self.BASE_URL), json={'product_name': "Nyundo", 'product_price': 300, 'quantity': "1"}, headers={
                'Content-Type': 'application/json'})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'], 'Bad request. The quantity should be specified in digits')