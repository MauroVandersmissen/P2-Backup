import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie import Movie, movies

def group_movies_by_year(movies):
    return {year:[movie.title for movie in movies if movie.year==year] for year in {movie.year for movie in movies}}

print(group_movies_by_year(movies))