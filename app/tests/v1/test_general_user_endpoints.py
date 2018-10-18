"""Module contains tests to endpoints that 

are general to both the admin and the normal user
"""

from . import base_test
from . import helper_functions

class TestGeneralUsersEndpoints(base_test.TestBaseClass):
    """Class contains the general user, i.e. both admin

    and normal user, endpoints' tests
    """

    def test_retrieve_all_products(self):
        """Test GET /products - when products exist"""

        response = self.app_test_client.get(
            '{}/products'.format(self.BASE_URL))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['products'][0]['product_name'], self.PRODUCT['product_name'])

    def test_retrieve_specific_product(self):
        """Test GET /products/id - when product exist"""
            
        response = self.app_test_client.get(
            '{}/products/1'.format(self.BASE_URL))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(helper_functions.convert_response_to_json(
            response)['product_name'], self.PRODUCT['product_name'])