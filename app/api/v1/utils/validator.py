import re

from flask import make_response, jsonify, abort
from validate_email import validate_email

from app.api.v1.models import users


class Validator:
    def validate_credentials(self, data):
        self.email = data["email"]
        self.password = data["password"]
        self.role = data["role"]
        valid_email = validate_email(self.email)
        for user in users.USERS:
            if self.email == user["email"]:
                Message = "User already exists"
                abort(406, Message)
        if self.email == "" or self.password == "" or self.role == "":
            Message = "You are missing a required credential"
            abort(400, Message)
        if not valid_email:
            Message = "Invalid email"
            abort(400, Message)
        elif len(self.password) < 6 or len(self.password) > 12:
            Message = "Password must be long than 6 characters or less than 12"
            abort(400, Message)
        elif not any(char.isdigit() for char in self.password):
            Message = "Password must have a digit"
            abort(400, Message)
        elif not any(char.isupper() for char in self.password):
            Message = "Password must have an upper case character"
            abort(400, Message)
        elif not any(char.islower() for char in self.password):
            Message = "Password must have a lower case character"
            abort(400, Message)
        elif not re.search("^.*(?=.*[@#$%^&+=]).*$", self.password):
            Message = "Password must have a special charater"
            abort(400, Message)
