"""Модель пользователей"""
from app.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user):
        return self.session.query(User).filter(User.username == user).one()

    def get_id(self, id):
        return self.session.query(User).get(id)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()

    def delete(self, id):
        user = self.get_id(id)

        self.session.delete(user)
        self.session.commit()
