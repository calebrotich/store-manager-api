"""This module contains endpoints

that are specific to the store attendant
"""
from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from . import helper_functions
from ..models import products, sale_orders
from . import verify

class SaleRecords(Resource):
    """Class contains the tests for store attendant
    
    specific endpoints
    """

    def post(self):
        """POST /saleorder endpoint"""

        # verify.verify_tokens()

        data = request.get_json()
        helper_functions.no_json_in_request(data)
        try:
            product_name = data['product_name']
            product_price = data['product_price']
            quantity = data['quantity']
        except KeyError:
            # If product is missing required parameter
            helper_functions.missing_a_required_parameter()

        if not isinstance(product_price, int):
            abort(make_response(jsonify(
                message="Bad request. The product price should be digits"
            ), 400))

        if product_price < 1:
            abort(make_response(jsonify(
                message="Bad request. Price of the product should be a positive integer above 0."
            ), 400))

        if not isinstance(product_name, str):
            abort(make_response(jsonify(
                message="Bad request. Product name should be a string"
            ), 400))


        if not isinstance(quantity, int):
            abort(make_response(jsonify(
                message="Bad request. The quantity should be specified in digits"
            ), 400))
        strip_product_name = product_name.strip()
        sale_order = sale_orders.SaleOrder(strip_product_name, product_price, quantity)
        sale_order.save()

        return make_response(jsonify({
            "message": "Checkout complete",
            "saleorder": {
                "product_name": product_name,
                "product_price": product_price,
                "quantity": quantity,
                "amount": (product_price * quantity)
            }
        }), 201)
