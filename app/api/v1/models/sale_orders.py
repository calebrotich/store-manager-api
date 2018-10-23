"""This module contains the data store

and data logic of the store attendant's sale orders
"""
from flask import jsonify

SALE_ORDERS = []

class SaleOrder():
    def __init__(self, product_name, product_price, quantity):
        self.id = len(SALE_ORDERS) + 1
        self.product_name = product_name
        self.product_price = product_price
        self.quantity = quantity

    def save(self):
        new_sale_order = {
            "sale_order_id": self.id,
            "product_name": self.product_name,
            "product_price": self.product_price,
            "quantity": self.quantity,
            "amount": (self.product_price * self.quantity)
            }
            
        SALE_ORDERS.append(new_sale_order)
        return new_sale_order