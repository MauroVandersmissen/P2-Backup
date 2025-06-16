# def closest(points, target_point):
#     min_distance = float('inf')
#     closest_point = None

#     for point in points:
#         distance = ((point[0] - target_point[0]) ** 2 + (point[1] - target_point[1]) ** 2) ** 0.5
#         if distance < min_distance:
#             min_distance = distance
#             closest_point = point

#     return closest_point

def closest(points, target_point):
    return min(points, key = lambda point: ((point[0] - target_point[0]) ** 2 + (point[1] - target_point[1]) ** 2) ** 0.5)

points = [(1, 9), (4, 3), (9, 5)]
target_point = (5, 7)

print(closest(points, target_point))