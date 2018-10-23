import os
import datetime
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)

from instance import config
from app.api.v1.utils.validator import Validator
from app.api.v1.models import users

class SignUp(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                                    "message": "Missing required credentials"
                                    }), 400)
        email = data["email"].strip()
        password = generate_password_hash(data["password"].strip(), method='sha256')
        role = data["role"].strip()
        Validator.validate_credentials(self, data)
        user = users.User_Model(email, password, role)
        res = user.save()
        return make_response(res, 202)


class Login(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                "message": "Kindly enter your credentials"
            }
            ), 400)
        email = data["email"]
        password = data["password"]

        for user in users.USERS:
            if email == user["email"] and check_password_hash(user["password"], password):
                token = jwt.encode({
                    "email": email,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta
                                  (minutes=5)
                }, os.getenv('JWT_SECRET_KEY', default='SdaHv342nx!jknr837bjwd?c,lsajjjhw673hdsbgeh'))
                return make_response(jsonify({
                             "message": "You are successfully logged in",
						     "token": token.decode("UTF-8")}), 200)
        return make_response(jsonify({
            "message": "Wrong credentials provided"
        }
        ), 403)
