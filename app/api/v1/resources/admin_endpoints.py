"""This module contains endpoints

that are specific to the admin
"""
from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource

from . import helper_functions
from app.api.v1.models import products

class AdminActs(Resource):
    """Class contains the tests for admin
    
    specific endpoints
    """


    def post(self):
        """POST /products endpoint"""
                  
        data = request.get_json()
        helper_functions.no_json_in_request(data)
        try:
            product_name = data['product_name']
            product_price = data['product_price']
            category = data['category']
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

        if not isinstance(category, str):
            abort(make_response(jsonify(
                message="Bad request. The Category should be a string"
            ), 400))

        if products.PRODUCTS:
            # If products are in the store already
            try:
                # Check if a product with a similar name exists
                existing_product = [
                    product for product in products.PRODUCTS if product['product_name'] == product_name][0]

                abort(make_response(jsonify({
                    "message": "Product with a similar name already exists",
                    "product": existing_product}), 400))

            except IndexError:
                # If there is no product with the same name
                response = helper_functions.add_new_product(product_name, product_price, category)
        else:
            # If there are no products in the store
            response = helper_functions.add_new_product(product_name, product_price, category)

        return response
