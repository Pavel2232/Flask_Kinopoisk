"""Вью режиссеров"""
from flask_restx import Namespace, Resource
from flask import request
from app.models.director import DirectorSchema
from app.constants import director_service

director_ns = Namespace('director')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many= True)

@director_ns.route('/')
class DirectorView(Resource):

    def get(self):
        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:id>')
class DirectorView(Resource):
    def put(self,id):
        req_json = request.json
        req_json["id"] = id

        director_service.update(req_json)

        return "", 204

    def patch(self,id):
        req_json = request.json
        req_json["id"] = id

        director_service.update_path(req_json)

        return "", 204

    def delete(self,id):
        director_service.delete(id)
        return "",204