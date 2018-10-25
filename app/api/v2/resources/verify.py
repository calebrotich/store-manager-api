import os
import jwt
from functools import wraps

from flask import request, make_response, jsonify, abort
from ..models import users


def verify_tokens():
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization']
    if not token:
        abort(make_response(jsonify({
                                "Message": "You need to login"}), 401))
    try:
        data = jwt.decode(token, os.getenv('JWT_SECRET_KEY', default='SdaHv342nx!jknr837bjwd?c,lsajjjhw673hdsbgeh'))
        return data["email"]

    except:
        abort(make_response(jsonify({
            "Message": "The token is either expired or wrong"
        }), 403))    



def verify_post_product_fields(product_price, product_name, category):
    if not isinstance(product_price, int):
        abort(make_response(jsonify(
            message="Product price should be an integer"
        ), 400))

    if product_price < 1:
        abort(make_response(jsonify(
            message="Price of the product should be a positive integer above 0."
        ), 400))

    if not isinstance(product_name, str):
        abort(make_response(jsonify(
            message="Product name should be a string"
        ), 400))

    if not isinstance(category, str):
        abort(make_response(jsonify(
            message="Bad request. The Category should be a string"
        ), 400))