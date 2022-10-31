"""Вью аунтификации"""

from flask_restx import Namespace, Resource, abort
from flask import request

from app.decorators import admin_required
from app.models.user import UserSchema
from app.constant import user_service, auth_service

auth_ns = Namespace('auth')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        user = request.json

        username = user.get("username", None)
        password = user.get("password", None)

        if None in [username, password]:
            return abort(400)

        user_service.create(user)

        return "", 201


@auth_ns.route('/login')
class AuthView(Resource):

    def post(self):
        data = request.json

        username = data.get("username", None)
        password = data.get("password", None)

        if None in [username, password]:
            return abort(400)

        tokens = auth_service.generate_token(username, password)

        return tokens, 201

    def put(self):
        data = request.json
        token = data.get("refresh_token")

        refrhesh_token = auth_service.approve_refresh_token(token)

        return refrhesh_token, 201


@auth_ns.route('/<int:id>')
class AuthView(Resource):

    @admin_required
    def put(self, id):
        req_json = request.json
        req_json["id"] = id

        user_service.update(req_json)

        return "", 204

    @admin_required
    def patch(self, id):
        req_json = request.json
        req_json["id"] = id

        user_service.update_path(req_json)

        return "", 204

    @admin_required
    def delete(self, id):
        user_service.delete(id)
        return "", 204
