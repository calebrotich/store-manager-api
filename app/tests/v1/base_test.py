"""
    Contains the base test class for the
    other test classes
"""
import unittest

# local imports
from app import create_app
from instance.config import config


class TestBaseClass(unittest.TestCase):
    """Base test class"""


    def setUp(self):
        """Create and setup the application

        for testing purposes
        """
        self.app = create_app('testing')
        self.BASE_URL = 'api/v1'
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app_test_client = self.app.test_client()
        self.app.testing = True

        self.PRODUCT = {
        'product_name': 'Phone Model 1',
        'product_price': 55000,
        'category': 'Phones'
        }

        self.SALE_ORDERS = {
        'product_name': 'Phone Model 1',
        'product_price': 55000,
        'quantity': 6,
        'amount': (55000 * 6)
        }


    def tearDown(self):
        """Destroy the application that

        is created for testing
        """
        self.app_context.pop()


if __name__ == '__main__':
    unittest.main()