"""Вью любимых жанров"""
from flask_restx import Namespace, Resource

from app.decorators import auth_required
from app.models.favorite_genre import GenreFSchema
from app.constant import genre_service

genre_ns = Namespace('favorites')

genref_schema = GenreFSchema()
genrefs_schema = GenreFSchema(many=True)


@genre_ns.route('/movies/<int:id>')
class GenreFView(Resource):

    @auth_required
    def post(self, id):
        film = genre_service.get_one(id)

        genre_service.update(film)

        return "", 204

    @auth_required
    def delete(self, id):
        genre_service.delete(id)
        return "", 204
