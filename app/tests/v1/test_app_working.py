"""
    Module contains tests for the working
    of the application
"""
from flask import current_app

#local imports
from . import base_test

class TestConfigCase(base_test.TestBaseClass):
   

    def test_app_exists(self):
        self.assertFalse(current_app is None)


    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])