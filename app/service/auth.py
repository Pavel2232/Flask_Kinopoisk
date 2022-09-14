"""Сервис пользователей"""
import calendar
import datetime

import jwt
from flask import current_app
from flask_restx import abort



class AuthService:
    def __init__(self, user_service):

        self.user_service = user_service

    def chek_user_and_creat(self, data):
        username = data.get("username", None)
        password = data.get("password", None)

        if None in [username, password]:
            return "", 400

        if not self.user_service.get_one(data.get("id")):
            user = self.user_service.create(data)

        else:
            return "Пользователь уже есть", 201

        return self.generate_token(data)

    def generate_token(self, username, password, is_refresh=False):
        user = self.user_service.get_one(username)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {"username": user.username,
                "role": user.role
                }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config["TOKEN_EXPIRE_MINUTES"])
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, current_app.config["SECRET"], algorithm=current_app.config["ALGO"])

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config["TOKEN_EXPIRE_DAY"])
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, current_app.config["SECRET"], algorithm=current_app.config["ALGO"])

        return {"access_token": access_token,
                "refresh_token": refresh_token
                }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=current_app.config["SECRET"], algorithm=current_app.config["ALGO"])
        username = data.get("username")

        return self.generate_token(username, None, is_refresh=True)
