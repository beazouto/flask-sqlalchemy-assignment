from flask_sqlalchemy import SQLAlchemy
from src.models import movie,db


class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        return movie.query.all()

    def get_movie_by_id(self, id):
        # TODO get a single movie from the DB using the ID
       
        return movie.query.get(id)

    def create_movie(self, title1, director, rating):
        # TODO create a new movie in the DB
        new_rating = movie(title = title1, director=director,rating=rating)
        db.session.add(new_rating)
        db.session.commit()
        return new_rating

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return movie.query.filter_by(title=title).all()


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
