"""Сервис пользователей"""
import base64
import calendar
import datetime
import hashlib
import hmac
import jwt
from app.dao.user import UserDAO
# from app.constant import PWD_HASH_SALT,PWD_HASH_ITERATIONS, secret , algo
PWD_HASH_SALT: bytes = b'secret here'
PWD_HASH_ITERATIONS = 100_000
secret = 's3cR$eT'
algo = 'HS256'



class UserService:
    def __init__(self, dao:UserDAO):

        self.dao = dao

    def get_hash(self,password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.make_user_password_hash(data.get("password"))
        return self.dao.create(data)

    def update(self, data):
        id = data.get("id")
        user = self.get_one(id)

        user.id = data.get("id")
        user.username =data.get("username")
        user.password =data.get("password")
        user.role =data.get("role")

        self.dao.update(user)

    def update_path(self, data):
        data["password"] = self.make_user_password_hash(data["password"])
        self.dao.update(data)
        return self.dao

    def delete(self, id):
        self.dao.delete(id)

    def make_user_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password, PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )
