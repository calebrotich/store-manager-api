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
    if user_role!= "Admin":
        abort(make_response(jsonify(
            message="Unauthorized. This action is not for you"
        ), 401))