"""Импортируем сервисы дао сессии бд"""
from app.dao.director import DirectorDAO
from app.dao.movie import MovieDAO
from app.dao.genre import GenreDAO
from app.service.director import DirectorService
from app.service.genre import GenreService
from app.service.movie import MovieService

from app.setup_db import db

movies_dao = MovieDAO(db.session)
movies_service = MovieService(movies_dao)


director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)



