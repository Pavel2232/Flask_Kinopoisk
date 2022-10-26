"""Модель любимых жанров"""
from app.models.favorite_genre import GenreF


class GenreFDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(GenreF).get(id)


    def create(self, data):
        genref = GenreF(**data)

        self.session.add(data)
        self.session.commit()

        return genref


    def delete(self, id):
        genref = self.get_one(id)

        self.session.delete(genref)
        self.session.commit()
