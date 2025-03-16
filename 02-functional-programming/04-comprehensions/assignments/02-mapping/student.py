import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie import Movie, movies

def titles(movies):
    return [movie.title for movie in movies]

def titles_and_years(movies):
    return [(movie.title,movie.year) for movie in movies]

def titles_and_actor_counts(movies):
    return [(movie.title,len(movie.actors)) for movie in movies]

def reverse_words(sentence):
    words=sentence.split(" ")
    reverse=[word[::-1] for word in words]
    return " ".join(reverse)

print(titles(movies))
print(titles_and_years(movies))
print(titles_and_actor_counts(movies))
print(reverse_words("Potato is God"))