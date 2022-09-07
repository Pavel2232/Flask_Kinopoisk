"""Сервис пользователей"""
import base64
import calendar
import datetime
import hashlib
import hmac
import sys

import jwt
from flask_restx import abort

# from app.constant import user_service
from app.dao.user import UserDAO

# from app.constant import PWD_HASH_SALT,PWD_HASH_ITERATIONS, secret , algo
PWD_HASH_SALT: bytes = b'secret here'
PWD_HASH_ITERATIONS = 100_000
secret = 's3cR$eT'
algo = 'HS256'



class AuthService:
    def __init__(self,user_service):

        self.user_service = user_service

    def chek_user_and_creat(self,data):
        username = data.get("username", None)
        password = data.get("password", None)

        if None in [username, password]:
            return "", 400

        if not self.user_service.get_one(data.get("id")):
            user = self.user_service.create(data)

        else:
            return "Пользователь уже есть", 201


        return self.generate_token(data)

    def generate_token(self,data, is_refresh= False):


        if not is_refresh:
            password = self.user_service.get_one(data.get("password"))
            if not self.user_service.compare_passwords(data.get("password"),password):
               abort(400)

        data = {"username": data.get("username"),
                "role": data.get("role")
                }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)


        return  {"access_token":access_token,
                "refresh_token":refresh_token
                }

    def approve_refresh_token(self,refresh_token):
        data = jwt.decode(jwt = refresh_token, key= secret, algorithms=[algo])
        username = data.get("username")

        return self.generate_token(username, is_refresh = True)



