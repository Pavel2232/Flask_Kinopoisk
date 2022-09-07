"""Импортируем сервисы дао сессии бд"""
from app.dao.director import DirectorDAO
from app.dao.movie import MovieDAO
from app.dao.genre import GenreDAO
from app.dao.user import UserDAO
from app.service.auth import AuthService
from app.service.director import DirectorService
from app.service.genre import GenreService
from app.service.movie import MovieService
from app.service.user import UserService

from app.setup_db import db

PWD_HASH_SALT: bytes = b'secret here'
PWD_HASH_ITERATIONS = 100_000
secret = 's3cR$eT'
algo = 'HS256'

movies_dao = MovieDAO(db.session)
movies_service = MovieService(movies_dao)


director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)



