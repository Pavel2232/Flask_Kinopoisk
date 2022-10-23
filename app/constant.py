"""Импортируем сервисы дао сессии бд"""
from dao.director import DirectorDAO
from dao.genre_favorite import GenreFDAO
from dao.movie import MovieDAO
from dao.genre import GenreDAO
from dao.user import UserDAO
from service.auth import AuthService
from service.director import DirectorService
from service.favorite_genre import GenreFService
from service.genre import GenreService
from service.movie import MovieService
from service.user import UserService

from setup_db import db


movies_dao = MovieDAO(db.session)
movies_service = MovieService(movies_dao)


director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)

genref_dao = GenreFDAO(db.session)
genref_service = GenreFService(genref_dao)

