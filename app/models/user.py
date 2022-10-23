from setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String,nullable = False)
    username = db.Column(db.String(60))
    surname = db.Column(db.String(100))
    favorite_genre = db.Column(db.Integer,db.ForeignKey("genre_fav.id"))
    role = db.Column(db.String(30))


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str()
    password = fields.Str()
    username = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
    role = fields.Str()
