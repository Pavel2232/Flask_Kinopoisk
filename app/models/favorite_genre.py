"""Модель любимых жанров"""
from setup_db import db
from marshmallow import Schema, fields


class GenreF(db.Model):
    __tablename__ = 'genre_fav'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User")
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    movie = db.relationship("Movie")

class GenreFSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
