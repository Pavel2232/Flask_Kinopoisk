"""Сервис пользователей"""
import base64
import hashlib
import hmac

from flask import current_app

from dao.user import UserDAO



class UserService:
    def __init__(self, dao:UserDAO):

        self.dao = dao

    def get_hash(self,password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            current_app.config["PWD_HASH_SALT"],
            current_app.config["PWD_HASH_ITERATIONS"]
        ).decode("utf-8", "ignore")

    def get_one(self, email):
        return self.dao.get_one(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.make_user_password_hash(data.get("password"))
        return self.dao.create(data)

    def update(self, data):
        email = data.get("email")
        user = self.get_one(email)


        user.username =data.get("email")
        user.password =data.get("password")
        user.role =data.get("username")
        user.role =data.get("surname")
        user.role =data.get("favorite_genre")
        user.role =data.get("role")

        self.dao.update(user)

    def update_path(self, data):
        email = data.get("email")
        user = self.get_one(email)

        if "email" in data:
            user.id = data.get("email")
        if "password" in data:
            user.password = self.make_user_password_hash(data["password"])
        if "username" in data:
            user.description = data.get("username")
        if "surname" in data:
            user.trailer = data.get("surname")
        if "favorite_genre" in data:
            user.year = data.get("favorite_genre")
        if "role" in data:
            user.rating = data.get("role")

        self.dao.update(data)
        return self.dao

    def delete(self, id):
        self.dao.delete(id)

    def make_user_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            current_app.config["PWD_HASH_SALT"],
            current_app.config["PWD_HASH_ITERATIONS"]
        ))

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password.encode(),current_app.config["PWD_HASH_SALT"],current_app.config["PWD_HASH_ITERATIONS"])
        )
