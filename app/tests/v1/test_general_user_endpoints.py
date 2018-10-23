"""Module contains tests to endpoints that 

are general to both the admin and the normal user
"""

import json

from . import base_test
from . import helper_functions

class TestGeneralUsersEndpoints(base_test.TestBaseClass):
    """Class contains the general user, i.e. both admin

    and normal user, endpoints' tests
    """


    def test_retrieve_all_products(self):
        """Test GET /products - when products exist"""

        self.register_test_admin_account()
        token = self.login_test_admin()

        response = self.app_test_client.get(
            '{}/products'.format(self.BASE_URL),
            headers=dict(Authorization=token),
            content_type='application/json'
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['products'][0]['product_name'], self.PRODUCT['product_name'])

    def test_retrieve_specific_product(self):
        """Test GET /products/id - when product exist"""

        self.register_test_admin_account()
        token = self.login_test_admin()

        response = self.app_test_client.get(
            '{}/products/1'.format(self.BASE_URL),
            headers=dict(Authorization=token),
            content_type='application/json'
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['product'], self.PRODUCT['product_name'])

    def test_retrieve_specific_sale_order(self):
        """Test GET /saleorder/id - when saleorder exists"""

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
            '{}/saleorder/1'.format(self.BASE_URL),
            headers=dict(Authorization=token),
            content_type='application/json'
            )

        self.assertEqual(response.status_code, 200)


    def test_missing_token(self):
        """Test GET /products - when token is missing"""

        self.register_test_admin_account()
        token = ""

        response = self.app_test_client.get(
            '{}/products'.format(self.BASE_URL),
            headers=dict(Authorization=token),
            content_type='application/json'
            )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)["Message"], "You need to login")


    def test_invalid_token(self):
        """Test GET /products - when token is missing"""

        self.register_test_admin_account()
        token = "sample_invalid-token-afskdghkfhwkedaf-ksfakjfwey"

        response = self.app_test_client.get(
            '{}/products'.format(self.BASE_URL),
            headers=dict(Authorization=token),
            content_type='application/json'
            )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)["Message"], "The token is either expired or wrong")