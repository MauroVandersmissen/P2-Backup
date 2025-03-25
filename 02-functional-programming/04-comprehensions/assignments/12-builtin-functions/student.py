import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie import Movie, movies

def movie_count(movie,director):
    return len([movie for movie in movies if movie.director==director])

def longest_movie_runtime_with_actor(movies,actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies,director,genre):
    return any(movie.director==director and genre in movie.genres for movie in movies)

def is_prime(n):
    return n>1 and not any(n%i==0 for i in range(2,int(math.sqrt(n))+1))

def is_increasing(ns):
    return all(ns[i]<=ns[i+1] for i in range(len(ns)-1))

def count_matching(xs,ys):
    return sum(1 for x,y in zip(xs,ys) if x==y)

def weighted_sum(ns,weights):
    return sum(n*weight for n,weight in zip(ns,weights))

def alternating_caps(string):
    return "".join(char.upper() if i%2==0 else char.lower() for i,char in enumerate(string))

# def find_repeated_words(sentence):
#     current_word=""
#     seen_words=set()
#     repeated_words=set()
#     for char in sentence:
#         if char.isalpha():
#             current_word+=char.lower()
#         elif current_word:
#             if current_word in seen_words:
#                 repeated_words.add(current_word)
#             else:
#                 seen_words.add(current_word)
#             current_word=""
#     if current_word:
#         if current_word in seen_words:
#             repeated_words.add(current_word)
#         else:
#             seen_words.add(current_word)
#     return repeated_words

def find_repeated_words(sentence):
    words=sentence.lower().split()
    alpha_words=[word.strip(",.") for word in words if word.strip(",.").isalpha()]
    print(alpha_words)
    return {alpha_words[i] for i in range(1,len(alpha_words)) if alpha_words[i] == alpha_words[i-1]}
# error, ignores words with , or . after it

print(movie_count(movies,"Coen Brothers"))
print(longest_movie_runtime_with_actor(movies,"Tom Cruise"))
print(has_director_made_genre(movies,"Paul Thomas Anderson","Drama"))
print(is_prime(7))
print(is_increasing([1,2,3,4,5]))
print(count_matching([1,2,3],[3,2,1]))
print(weighted_sum([1,2,3],[4,5,6]))
print(alternating_caps("abcdef"))
print(find_repeated_words("This sentence has has repeated words. Words."))
print(find_repeated_words("this is, is a test this is also a test"))