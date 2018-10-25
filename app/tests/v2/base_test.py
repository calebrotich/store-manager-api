"""
    Contains the base test class for the
    other test classes
"""
import unittest

# local imports
from app import create_app
from instance.config import config
from . import helper_functions
from ...api.v2.database import init_db
from instance.config import config


class TestBaseClass(unittest.TestCase):
    """Base test class"""


    def setUp(self):
        """Create and setup the application

        for testing purposes
        """
        self.app = create_app('testing')
        self.BASE_URL = 'api/v2'
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app_test_client = self.app.test_client()
        self.app.testing = True

        with self.app.app_context():
            self.db_url = config['test_db_url']
            init_db(self.db_url)

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
        with self.app.app_context():
            init_db(self.db_url)
        self.app_context.pop()

    def register_test_admin_account(self):
        #Register attendant
        """Registers an admin test user account"""
            
        res = self.app_test_client.post("api/v2/auth/signup",
        json={
        "email": "user@gmail.com",
        "role": "admin",
        "password": "Password12#"
        }, 
        headers={
        "Content-Type": "application/json"
        })

        return res
    
    def login_test_admin(self):
        """Validates the test account for the admin"""

        # Login the test account for the admin
        resp = self.app_test_client.post("api/v2/auth/login",
        json={
            "email": "user@gmail.com",
            "password": "Password12#"
        },
        headers={
        "Content-Type": "application/json"
        })

        auth_token = helper_functions.convert_response_to_json(
        resp)['token']

        return auth_token

if __name__ == '__main__':
    unittest.main()