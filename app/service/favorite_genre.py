"""Сервис любимых жанров"""
from dao.genre_favorite import GenreFDAO


class GenreFService:
    def __init__(self, dao: GenreFDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)


    def create(self, data):

        return self.dao.create(data)


    def delete(self, id):
        self.dao.delete(id)

