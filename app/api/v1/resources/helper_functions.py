from datetime import datetime
from flask import abort, jsonify, make_response

from app.api.v1.models import products

def no_json_in_request(data):
    """Aborts if the data does

    not contain a json object      
    """
        
    if data is None:
        # If a json was not obtained from the request
        abort(make_response(jsonify(
            message="Bad request. Request data must be in json format"), 400))


def missing_a_required_parameter():
    """Aborts if request data is missing a

    required argument
    """
    abort(make_response(jsonify(
        message="Bad request. Request missing a required argument"), 400))


def add_new_product(name, price, category):
    """Creates a new product"""

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
        # if any of the required parameterss is missing or none
        missing_a_required_parameter()
    return response
