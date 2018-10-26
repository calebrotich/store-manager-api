"""This module contains endpoints

for both the admin and the normal user
"""
from flask import jsonify, abort, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from . import verify

from . import helper_functions
from app.api.v1.models import products, sale_orders

class AllProducts(Resource):
    """Class contains the tests for both

    the admin and the normal user endpoints
    """

    def get(self):
        """GET /products endpoint"""
        verify.verify_tokens()
        if not products.PRODUCTS:
            # If no products exist in the store yet
            abort(make_response(
                jsonify(message="There are no products in the store yet"), 404))
        # if at least one product exists
        response = jsonify({
            'message': "Successfully fetched all the products",
            'products': products.PRODUCTS
            })
        response.status_code = 200
        return response

class SpecificProduct(Resource):

    def get(self, product_id):

        verify.verify_tokens()

        for product in products.PRODUCTS:
            if product["product_id"] == product_id:
                return make_response(jsonify({
                    "message": "{} retrieved successfully".format(product["product_name"]),
                    "product": product
                }
                ), 200)

            else:
                return make_response(jsonify({
                    "message": "Product with id {} not found".format(product_id)
                }
                ), 404)


class SpecificSaleOrder(Resource):

    def get(self, sale_order_id):
        """GET /saleorder/<int:sale_order_id>"""

        verify.verify_tokens()
        
        for sale_order in sale_orders.SALE_ORDERS:
            if sale_order["sale_order_id"] == sale_order_id:
                return make_response(jsonify({
                    "message": "Sale Order with Id {} retrieved successfully".format(sale_order["sale_order_id"]),
                    "product": sale_order
                }
                ), 200)

        return make_response(jsonify({
            "message": "Sale Order with id {} not found".format(sale_order_id)
        }
        ), 404)