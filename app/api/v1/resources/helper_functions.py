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



def retrieve_specific_product(product_id):
    """
        Helper method to fetch product from list of products,
        given valid id
    """
    specific_product = None
    for product in products.PRODUCTS:
        if product['product_id'] == product_id:
            specific_product = product
            break
    if not specific_product:
        abort_if_item_is_not_found(product_id)

    return specific_product

def retrieve_specific_sale_order(sale_id):
    """
        Helper method to fetch sale order from list of sale orders,
        given a valid id
    """
    specific_sale_order = None
    for sale_order in sale_orders.SALE_ORDERS:
        if sale_order['sale_order_id'] == sale_id:
            specific_sale_order = sale_order
            break
    if not specific_sale_order:
        abort_if_item_is_not_found(sale_id)

    return specific_sale_order

def abort_if_item_is_not_found(item_id):
    """
        Helper method to search for Product
        Abort if product not found and throw error
    """
    abort(make_response(jsonify(
        message="Item with id {} not found".format(item_id)), 404))


def add_new_sale_record(name, price, quantity, amount):

    """Creates a new sale record"""

    if name and price and quantity and amount:
        # If all the required parameters are available
        sale_order_id = len(sale_orders.SALE_ORDERS) + 1
        sale_order = {
            'sale_order_id': sale_order_id,
            'product_name': name,
            'product_price': price,
            'quantity': quantity,
            'amount': amount,
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        sale_orders.SALE_ORDERS.append(sale_order)
        response = jsonify({
            "message": "Sale record added successfully",
            "sale_order": sale_orders.SALE_ORDERS[-1]})
        response.status_code = 201
    else:
        # if any of the required parameters is missing or none
        missing_a_required_parameter()
    return response

def abort_if_user_is_not_admin(user):
    user_role = [users['role'] for users in users.USERS if users['email'] == user][0]
    if user_role!= "Admin":
        abort(make_response(jsonify(
            message="Unauthorized. This action is not for you"
        ), 401))