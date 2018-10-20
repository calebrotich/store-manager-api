"""This module contains endpoints

for both the admin and the normal user
"""
from flask import jsonify, abort, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from . import helper_functions
from app.api.v1.models import products

class AllProducts(Resource):
    """Class contains the tests for both

    the admin and the normal user endpoints
    """

    def get(self):
        """GET /products endpoint"""
        
        if not products.PRODUCTS:
            # If no products exist in the store yet
            abort(make_response(
                jsonify(message="There are no products in the store yet"), 404))
        # if at least one product exists
        response = jsonify({'products': products.PRODUCTS})
        response.status_code = 200
        return response

class SpecificProduct(Resource):

    def get(self, product_id):
        """GET /products/<int:product_id>"""
            
        product = helper_functions.retrieve_specific_product(product_id)
        response = jsonify(product)
        response.status_code = 200

        return response


class SpecificSaleOrder(Resource):

    @jwt_required
    def get(self, sale_order_id):
        """GET /saleorder/<int:sale_order_id>"""

        sale_order = helper_functions.retrieve_specific_sale_order(sale_order_id)
        response = jsonify(sale_order)
        response.status_code = 200