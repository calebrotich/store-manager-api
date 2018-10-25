"""This module contains endpoints

for both the admin and the normal user
"""
from flask import jsonify, abort, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from . import verify

from . import helper_functions
from ..models import products, sale_orders
from .. import database

class AllProducts(Resource):
    """Class contains the tests for both

    the admin and the normal user endpoints
    """

    def get(self):
        """GET /products endpoint"""
        verify.verify_tokens()
        query = """SELECT * FROM products"""
        fetched_products = products.Products.fetch_products(query)
        if not fetched_products:
            return make_response(jsonify({
                "message": "There are no products in the store yet",
                }), 404)

        response = jsonify({
            'message': "Successfully fetched all the products",
            'products': fetched_products
            })

        response.status_code = 200
        return response

class SpecificProduct(Resource):

    def get(self, product_id):

        # verify.verify_tokens()
        query = """SELECT * FROM products WHERE product_id = '{}'""".format(product_id)

        fetched_product = database.select_from_db(query)
        if not fetched_product:
            return make_response(jsonify({
            "message": "Product with id {} is not available".format(product_id),
            }), 400)
        
        return make_response(jsonify({
            "message": "{} retrieved successfully".format(fetched_product[0][1]),
            "product": fetched_product
            }), 200)
        

class SpecificSaleOrder(Resource):

    def get(self, sale_order_id):
        """GET /saleorder/<int:sale_order_id>"""

        # verify.verify_tokens()
        query = """SELECT * FROM saleorders WHERE sale_order_id = '{}'""".format(sale_order_id)
        sale_order = database.select_from_db(query)
        if not sale_order:
            return make_response(jsonify({
                "message": "Sale Order with id {} not found".format(sale_order_id)
            }
            ), 404)

        return make_response(jsonify({
            "message": "Sale order fetched successfully",
            "saleorder": sale_order
        }
        ), 200)