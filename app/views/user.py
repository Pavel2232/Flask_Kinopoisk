import jwt
from flask_restx import Namespace, Resource, abort
from flask import request
from app.models.user import UserSchema
from app.constant import user_service, auth_service
import datetime
import calendar




user_ns = Namespace('user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    def post(self):
        user = request.json

        username= user.get("username",None)
        password= user.get("password",None)

        if None in [username,password]:
            return abort(400)

        user_service.create(user)

        return "",201