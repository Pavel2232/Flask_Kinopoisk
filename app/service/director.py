"""Сервис рижесёров"""
from app.dao.director import DirectorDAO

class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create()

    def update(self, data):
        id = data.get("id")
        director = self.get_one(id)

        director.id = data.get("id")
        director.name = data.get("name")

        self.dao.update(director)

    def update_path(self, data):
        id = data.get("id")
        director = self.get_one(id)
        if "id" in data:
            director.id = data.get("id")
        if "name" in data:
            director.id = data.get("name")

        self.dao.update(director)

    def delete(self, id):
        self.dao.delete(id)