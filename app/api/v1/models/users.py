from flask import make_response, jsonify
USERS = []


class User_Model():
    def __init__(self, email, password, role):
        self.id = len(USERS) + 1
        self.email = email
        self.password = password
        self.role = role

    def save(self):
        new_user = {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "role": self.role
            }

        new_added_user = {
            "id": self.id,
            "email": self.email,
            "role": self.role
            }
            
        USERS.append(new_user)
        return new_added_user