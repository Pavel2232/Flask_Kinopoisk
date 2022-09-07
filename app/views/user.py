"""Вью аунтификации"""
import jwt
from flask_restx import Namespace, Resource, abort
from flask import request
from app.models.user import UserSchema
from app.constant import user_service, auth_service
import datetime
import calendar




user_ns = Namespace('auth')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):

    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):

        data = request.json

        tokens = auth_service.chek_user_and_creat(data)

        return tokens, 201

    def put(self):
        data = request.json


        refrhesh_token =auth_service.approve_refresh_token(data)

        return refrhesh_token, 201


@user_ns.route('/<int:id>')
class UserView(Resource):
    def put(self, id):
        req_json = request.json
        req_json["id"] = id

        user_service.update(req_json)

        return "", 204

    def patch(self, id):
        req_json = request.json
        req_json["id"] = id

        user_service.update_path(req_json)

        return "", 204

    def delete(self, id):
        user_service.delete(id)
        return "", 204