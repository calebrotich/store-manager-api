"""This module contains endpoints

that are specific to the admin
"""
import os
from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from functools import wraps
import jwt

from . import helper_functions
from app.api.v1.models import products, sale_orders, users
from . import verify


class ProductsManagement(Resource):
    """Class contains the tests for admin
    
    specific endpoints
    """
    def post(self):
        """POST /products endpoint"""

        logged_user = verify.verify_tokens()
        helper_functions.abort_if_user_is_not_admin(logged_user)            
        
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
                added_product = products.Products(product_name, product_price, category)
                response = added_product.save()
        else:
            # If there are no products in the store
                added_product = products.Products(product_name, product_price, category)
                response = added_product.save()

        return make_response(jsonify({
            "message": "Product added successfully",
            "product": response
        }), 201)


class SaleAttendantsManagement(Resource):
    """Class contains the tests managing

    sale orders
    """

    def get(self):
        """GET /saleorder endpoint"""

        verify.verify_tokens()
        
        if not sale_orders.SALE_ORDERS:
            # If no products exist in the store yet
            abort(make_response(
                jsonify(message="There are no sale orders made yet"), 404))
        # if at least one product exists
        response = jsonify({
            'message': "Successfully fetched all the sale orders",
            'sale_orders': sale_orders.SALE_ORDERS
            })
        response.status_code = 200
        return response
