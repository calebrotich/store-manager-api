"""This module contains the data store

and data logic of the store attendant's sale orders
"""
import datetime
from flask import jsonify

from .. import database

class SaleOrder():
    def __init__(self, product_name, product_price, quantity):
        self.product_name = product_name
        self.product_price = product_price
        self.quantity = quantity
        self.amount = (self.quantity * self.product_price)
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save(self):
        query = """
        INSERT INTO saleorders(product_name, product_price, quantity, amount, date_ordered) VALUES(
            '{}', '{}', '{}', '{}', '{}'
        )""".format(self.product_name, self.product_price, self.quantity, self.amount, self.date)

        database.insert_to_db(query)


    @staticmethod
    def fetch_saleorder(product_name):
        """
            Queries db for user with given username
            Returns user object
        """
        # Query db for user with those params
        query = """
        SELECT * FROM saleorders
        WHERE product_name = '{}'""".format(product_name)

        return database.select_from_db(query)