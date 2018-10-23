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
            for user in users.USERS:
                if user['email'] == data['email']:
                    logged_user = user

        except:
            print(os.getenv('JWT_SECRET_KEY', default='SdaHv342nx!jknr837bjwd?c,lsajjjhw673hdsbgeh'))
            abort(make_response(jsonify({
                "Message": "This token is invalid"
            }), 403))

        return logged_user["email"]