# from itertools import permutations
# import sys
# import os

# # Get the absolute path of the student.py file
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../02-total-distance'))
# sys.path.append(parent_dir)

# from student import distance

# ^ Deze code werkt niet omdat beide bestanden student.py zijn, code met verschillende bestand namen in 02-functional-programming\04-comprehensions\assignments\02-mapping\student.py

from itertools import permutations
import importlib.util
import sys
import os

# Build absolute path to the student.py in 02-total-distance
student_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../02-total-distance/student.py'))

# Create a module spec from the file location
spec = importlib.util.spec_from_file_location("student_external", student_path)
student_external = importlib.util.module_from_spec(spec)
sys.modules["student_external"] = student_external
spec.loader.exec_module(student_external)

# Now you can access functions from the external student.py as:
distance = student_external.distance
total_distance = student_external.total_distance  # if needed

from student import distance

def find_shortest_path(distance, city_count):
    cities = range(1, city_count)
    best_path = None
    shortest_distance = float("inf")

    for city in permutations(cities):
        path = [0] + list(city) + [0]
        total = sum(distance(path[i], path[i + 1]) for i in range (len(path) - 1))
        # print(f"Path: {path} total distance: {total}") # Test om te zien of het door elke path gaat
        if total < shortest_distance:
            shortest_distance = total
            best_path = path
    # print(f"Best path: {best_path} Total distance: {shortest_distance}") # Print best path met distance
    return best_path

# Nodig om test code (prints) van geïmporteerde modules te negeren en enkel uit te voeren als de file zelf wordt uitgevoerd
if __name__ == "__main__":
    print(find_shortest_path(distance, 4))