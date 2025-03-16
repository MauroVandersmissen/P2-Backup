import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie import Movie, movies

def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs,ys):
    return {x for x in xs if x in ys}

xs = [1, 2, 3, 4, 5]
ys = [3, 4, 5, 6, 7]
print(directors(movies))
print(common_elements(xs,ys))