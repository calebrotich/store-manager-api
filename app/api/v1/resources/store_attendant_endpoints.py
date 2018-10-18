"""This module contains endpoints

that are specific to the store attendant
"""
from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource

from . import helper_functions
from app.api.v1.models import products

class SaleRecords(Resource):
    """Class contains the tests for store attendant
    
    specific endpoints
    """


    def post(self):
        """POST /saleorder endpoint"""
                  
        data = request.get_json()
        helper_functions.no_json_in_request(data)
        try:
            product_name = data['product_name']
            product_price = data['product_price']
            quantity = data['quantity']
            amount = (product_price * quantity)
        except KeyError:
            # If product is missing required parameter
            helper_functions.missing_a_required_parameter()

        if product_price < 1:
            abort(make_response(jsonify(
                message="Bad request. Price of the product should be a positive integer above 0."
            ), 400))

        if not isinstance(product_name, str):
            abort(make_response(jsonify(
                message="Bad request. Product name should be a string"
            ), 400))

        if not isinstance(product_price, int):
            abort(make_response(jsonify(
                message="Bad request. The product price should be digits"
            ), 400))

        if not isinstance(quantity, int):
            abort(make_response(jsonify(
                message="Bad request. The quantity should be specified in digits"
            ), 400))

        response = helper_functions.add_new_sale_record(product_name, product_price, quantity, amount)

        return response