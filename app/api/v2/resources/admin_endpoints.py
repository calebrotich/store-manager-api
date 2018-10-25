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
from ..models import products, sale_orders, users
from . import verify
from .. import database
from ..utils import validator


class ProductsManagement(Resource):
    """Class contains admin specific endpoints"""
    
    
    def post(self):
        """POST /products endpoint"""

        # Token verification and admin user determination
        # logged_user = verify.verify_tokens()
        # helper_functions.abort_if_user_is_not_admin(logged_user)
        
        data = request.get_json()
        helper_functions.no_json_in_request(data)
        try:
            product_name = data['product_name']
            product_price = data['product_price']
            category = data['category']
        except KeyError:
            # If product is missing required parameter
            helper_functions.missing_a_required_parameter()

        validator.check_duplication("product_name", "products", product_name)
        verify.verify_post_product_fields(product_price, product_name, category)

        added_product = products.Products(product_name, product_price, category)
        added_product.save()

        return make_response(jsonify({
            "message": "Product added successfully",
            "product": {
                "product_name": product_name,
                "product_price": product_price,
                "category": category
            }
        }), 201)


class SaleAttendantsManagement(Resource):
    """Class contains the tests managing

    sale orders
    """

    def get(self):
        """GET /saleorder endpoint"""

        # verify.verify_tokens()
        
        query = """SELECT * FROM saleorders"""
        saleorders = database.select_from_db(query)
        if not saleorders:
            return jsonify({
            'message': "No sale orders created yet"
            })

        response = jsonify({
            'message': "Successfully fetched all the sale orders",
            'sale_orders': saleorders
            })
        response.status_code = 200
        return response
