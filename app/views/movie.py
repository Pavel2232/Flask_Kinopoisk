"""Вью фильмов"""
from flask_restx import Namespace, Resource
from flask import request

from decorators import auth_required, admin_required
from models.movie import MovieSchema
from constant import movies_service


movie_ns = Namespace('movie')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MovieView(Resource):

    @auth_required
    def get(self):
        all_movie = movies_service.get_all()
        return movies_schema.dump(all_movie), 200

    @admin_required
    def post(self):
        req_json = request.json
        movies_service.create(req_json)
        return "", 201



@movie_ns.route('/<int:id>')
class MovieView(Resource):
    @admin_required
    def put(self, id):
        req_json = request.json
        req_json["id"] = id

        movies_service.update(req_json)

        return "", 204

    @admin_required
    def patch(self, id):
        req_json = request.json
        req_json["id"] = id

        movies_service.update_path(req_json)

        return "", 204

    @admin_required
    def delete(self, id):
        movies_service.delete(id)
        return "", 204