"""Сервис жанров"""
from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        id = data.get("id")
        genre = self.get_one(id)

        genre.id = data.get("id")
        genre.name = data.get("name")

        self.dao.update(genre)

    def update_path(self, data):
        id = data.get("id")
        genre = self.get_one(id)
        if "id" in data:
            genre.id = data.get("id")
        if "name" in data:
            genre.id = data.get("name")

        self.dao.update(genre)

    def delete(self, id):
        self.dao.delete(id)
