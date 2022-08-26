"""Модель режисеров"""
from app.models.director import Director
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Director).get(id)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self,data):
        director = Director(**data)

        self.session.add(data)
        self.session.commit()

        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()


    def delete(self, id):
        director = self.get_one(id)

        self.session.delete(director)
        self.session.commit()