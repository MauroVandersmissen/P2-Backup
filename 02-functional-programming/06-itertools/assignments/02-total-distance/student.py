from itertools import pairwise

def distance(a, b):
    return abs(a - b)

def total_distance(path, distance):
    return sum(distance(a, b) for a, b in pairwise(path))

if __name__ == "__main__":
    path = [1, 4, 8, 2, 0, 3]
    print(total_distance(path, distance))