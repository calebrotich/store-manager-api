"""This module contains the data store

and data logic of the store's products
"""

PRODUCTS = []

class Products():
    def __init__(self, product_name, product_price, category):
        self.id = len(PRODUCTS) + 1
        self.product_name = product_name
        self.product_price = product_price
        self.category = category

    def save(self):
        new_product = {
            "product_id": self.id,
            "product_name": self.product_name,
            "product_price": self.product_price,
            "category": self.category
            }
            
        PRODUCTS.append(new_product)
        return new_product