from flask import Flask
from flask_restx import Api
from app.config import Config
from app.setup_db import db
from app.views.movie import movie_ns
from app.views.genre import genre_ns
from app.views.director import director_ns



def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application

def configur_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    # api.add_namespace(movie_ns)
    # api.add_namespace(genre_ns )
    api.add_namespace(director_ns)
    # create_data(application, db)
#
# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
# app = create_app(Config())
# app.debug = True
#
if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configur_app(app)
    app.run(debug=True)



