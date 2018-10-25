from flask import make_response, jsonify

from .. import database

class User_Model():
    def __init__(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

    def save(self):
        query = """
        INSERT INTO users(email, role, password) VALUES(
            '{}', '{}', '{}'
        )""".format(self.email, self.role, self.password)

        database.insert_to_db(query)

    @staticmethod
    def fetch_user(email):
        """
            Queries db for user with given username
            Returns user object
        """
        # Query db for user with those params
        query = """
        SELECT * FROM users
        WHERE email = '{}'""".format(email)

        return database.select_from_db(query)