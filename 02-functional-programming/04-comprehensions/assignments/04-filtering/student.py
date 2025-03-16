import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie import Movie, movies

def movies_from_year(movies,year):
    return [movie.title for movie in movies if movie.year==year]

def movie_with_actor(movies,actor):
    return [movie.title for movie in movies if actor in movie.actors]

def divisors(n):
    return sorted([i for i in range(1, int(n ** 0.5) + 1) if n % i == 0] + [n // i for i in range(1, int(n ** 0.5) + 1) if n % i == 0 and i != n // i])

print(movies_from_year(movies,1999))
print(movie_with_actor(movies,"Tom Cruise"))
print(divisors(12))