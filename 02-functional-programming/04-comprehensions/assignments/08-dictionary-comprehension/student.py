import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie import Movie, movies

def title_to_director(movies):
    return {movie.title:movie.director for movie in movies}

def director_to_titles(movies):
    return {director: [movie.title for movie in movies if movie.director == director] 
            for director in set(movie.director for movie in movies)}

print(title_to_director(movies))
print(director_to_titles(movies))