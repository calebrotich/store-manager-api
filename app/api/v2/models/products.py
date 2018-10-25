"""This module contains the data store

and data logic of the store's products
"""
from .. import database

class Products():
    def __init__(self, product_name, product_price, category):
        self.product_name = product_name
        self.product_price = product_price
        self.category = category


    def save(self):
        query = """
        INSERT INTO products(product_name, product_price, category) VALUES(
            '{}', '{}', '{}'
        )""".format(self.product_name, self.product_price, self.category)

        database.insert_to_db(query)

    @staticmethod
    def fetch_product(product_name):
        """
            Queries db for user with given username
            Returns user object
        """
        # Query db for user with those params
        query = """
        SELECT * FROM products
        WHERE product_name = '{}'""".format(product_name)

        return database.select_from_db(query)

    @staticmethod
    def fetch_products(query):
        return database.select_from_db(query)
