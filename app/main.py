from flask import Flask
from flask_restx import Api
from app.config import Config
from app.setup_db import db, migrate
from app.views.favorite_genre import genref_ns
from app.views.movie import movie_ns
from app.views.genre import genre_ns
from app.views.director import director_ns
from app.views.auth import  auth_ns
from app.views.user import user_ns


def create_app(config: Config)-> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    db.init_app(application)
    migrate.init_app(application, db)
    return application


def configur_app(application: Flask):
    api =Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(genref_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configur_app(app)
    app.run()
