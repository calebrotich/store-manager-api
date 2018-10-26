from datetime import datetime

from flask import abort, jsonify, make_response

from app.api.v1.models import products, sale_orders, users

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


def abort_if_user_is_not_admin(user):
    user_role = [users['role'] for users in users.USERS if users['email'] == user][0]
    if user_role!= "admin":
        abort(make_response(jsonify(
            message="Unauthorized. This action is not for you"
        ), 401))


def add_product_to_store(product_name, product_price, category):
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

    return response