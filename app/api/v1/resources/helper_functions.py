from datetime import datetime
from flask import abort, jsonify, make_response

from app.api.v1.models import products

def abort_if_no_json_from_request(req_data):
    """
        Helper function.
        Aborts if a json could not be obtained from request data
    """
    if req_data is None:
        # If a json was not obtained from the request
        abort(make_response(jsonify(
            message="Bad request. Request data must be in json format"), 400))


def abort_if_missing_required_param():
    """
        Helper function.
        Aborts if request data is missing a required argument
    """
    abort(make_response(jsonify(
        message="Bad request. Missing required param"), 400))


def add_new_product(name, price, category):
    """
        Helper function
        Makes a new order, and prepares the response as a json

    """
    if name and price and category:
        # If all the required parameters are available
        product_id = len(products.PRODUCTS) + 1
        product = {
            'product_id': product_id,
            'product_name': name,
            'product_price': price,
            'category': category,
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        products.PRODUCTS.append(product)
        response = jsonify({
            "message": "Product added successfully",
            "product": products.PRODUCTS[-1]})
        response.status_code = 201
    else:
        # if any of the required params is None
        abort_if_missing_required_param()
    return response
