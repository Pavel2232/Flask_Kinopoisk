import jwt
from flask_restx import Namespace, Resource, abort
from flask import request
from app.models.user import UserSchema
from app.constant import user_service

from app.decorators import admin_required

user_ns = Namespace('user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):


    @admin_required
    def get(self):
        data = request.json

        user = user_service.get_one("email")
        return users_schema.dump(user), 200


    @admin_required
    def patch(self):
        data = request.json

        user = user_service.update_path(data)

        return "", 201
