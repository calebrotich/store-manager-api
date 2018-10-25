import re

from flask import make_response, jsonify, abort
from validate_email import validate_email

from .. import database

class Validator:
    def validate_credentials(self, data):
        self.email = data["email"].strip()
        self.password = data["password"].strip()
        self.role = data["role"].strip()
        valid_email = validate_email(self.email)

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

def check_duplication(column, table, value):
    """
        Check if a param is already in use, abort if in use
    """
    query = """
    SELECT {} FROM {} WHERE {}.{} = '{}'
    """.format(column, table, table, column, value)

    duplicated = database.select_from_db(query)
    if duplicated:
        print(duplicated) 

        abort(make_response(jsonify(
            message="Record already exists in the database"), 400))
            
            
