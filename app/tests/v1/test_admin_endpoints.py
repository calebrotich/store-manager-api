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
        self.register_test_admin_account()
        token = self.login_test_admin()

        # send a dummy data response for testing
        response = self.app_test_client.post('{}/products'.format(
            self.BASE_URL), json=self.PRODUCT, headers=dict(Authorization=token),
            content_type='application/json')

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

    def test_add_new_product_parameter_missing(self):
        """Test POST /products

        with one of the required parameters missing
        """
        self.register_test_admin_account()
        token = self.login_test_admin()

        response = self.app_test_client.post('{}/products'.format(
            self.BASE_URL), json={'product_name': 'Nyundo'}, headers=dict(Authorization=token),
            content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'], 'Bad request. Request missing a required argument')

    def test_add_new_product_price_under_one(self):
        """Test POST /products

        with the price of the product below minimum
        """
        self.register_test_admin_account()
        token = self.login_test_admin()

        response = self.app_test_client.post('{}/products'.format(
            self.BASE_URL), json={
                'product_id': 1, 'product_name': "Hammer", 'product_price': 0, 'category':'Tools'
                }, headers=dict(Authorization=token),
                content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'],
            'Bad request. Price of the product should be a positive integer above 0.')


    def test_add_new_product_with_product_name_not_string(self):
        """Test POST /products

        with the product name not a string
        """
        self.register_test_admin_account()
        token = self.login_test_admin()

        response = self.app_test_client.post('{}/products'.format(
            self.BASE_URL), json={
                'product_id': 1, 'product_name': 200, 'product_price': 200, 'category':'Tools'
                }, headers=dict(Authorization=token),
                content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'],
            'Bad request. Product name should be a string')

    def test_add_new_product_with_category_not_string(self):
        """Test POST /products

        with the category not a string
        """
        self.register_test_admin_account()
        token = self.login_test_admin()

        response = self.app_test_client.post('{}/products'.format(
            self.BASE_URL), json={
                'product_id': 1, 'product_name': "Hammer", 'product_price': 200, 'category': 200
                }, headers=dict(Authorization=token),
                content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'],
            'Bad request. The Category should be a string')

    def test_add_new_product_with_product_name_already_existing(self):
        """Test POST /products

        with the product name already existing
        """
        self.register_test_admin_account()
        token = self.login_test_admin()

        self.app_test_client.post('{}/products'.format(
            self.BASE_URL), json={
                'product_id': 1, 'product_name': "Hammer", 'product_price': 200, 'category': "Tools"
                }, headers=dict(Authorization=token),
                content_type='application/json')

        response = self.app_test_client.post('{}/products'.format(
            self.BASE_URL), json={
                'product_id': 1, 'product_name': "Hammer", 'product_price': 200, 'category': "Tools"
                }, headers=dict(Authorization=token),
                content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['message'],
            'Product with a similar name already exists')


    def test_fetch_sale_orders(self):
        """Test GET /saleorder - when sale order exists"""
        self.register_test_admin_account()
        token = self.login_test_admin()

        self.app_test_client.post(
        '{}/saleorder'.format(self.BASE_URL), json={
            'sale_order_id': 1,
            'product_name': "Test Product",
            'product_price': 20,
            'quantity': 1,
            'amount': 20
        },
        headers=dict(Authorization=token),
        content_type='application/json')
                                                                
        response = self.app_test_client.get(
            '{}/saleorder'.format(self.BASE_URL),

            headers=dict(Authorization=token),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['sale_orders'][0]['product_name'], "Test Product")
        self.assertEqual(helper_functions.convert_response_to_json(
           response)['sale_orders'][0]['product_price'], 20)
