"""This module contains endpoints

that are specific to the admin
"""
import os
import jwt
from functools import wraps

from flask import Flask, jsonify, request, abort, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from . import helper_functions
from app.api.v1.models import products, sale_orders, users
from . import verify


class ProductsManagement(Resource):
    """Class contains the tests for admin
    
    specific endpoints
    """
    def post(self):
        """POST /products endpoint"""

        # Token verification and admin user determination
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

        verify.verify_post_product_fields(product_price, product_name, category)

        response = helper_functions.add_product_to_store(product_name, product_price, category)

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
