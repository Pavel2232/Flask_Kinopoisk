"""Вью жанров"""
from flask_restx import Namespace, Resource
from flask import request
from app.models.genre import GenreSchema
from app.constants import genre_service

genre_ns = Namespace('genre')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):

    def get(self):
        all_genre = genre_service.get_all()
        return genres_schema.dump(all_genre), 200

    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return "", 201

    def put(self, id):
        req_json = request.json
        req_json["id"] = id

        genre_service.update(req_json)

        return "", 204

    def patch(self, id):
        req_json = request.json
        req_json["id"] = id

        genre_service.update_path(req_json)

        return "", 204

    def delete(self, id):
        genre_service.delete(id)
        return "", 204
