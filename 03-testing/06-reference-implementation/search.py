class Student:
    def __init__(self, id):
        self.id = id

def linear_search(students, target_id):
        for student in students:
            if student.id == target_id:
                return student
        return None
            
def binary_search(students, target_id):
        left = 0
        right = len(students)
        

        while left < right:
            middle = (left + right) // 2
            id = students[middle].id
            if id < target_id:
                left = middle + 1
            elif id > target_id:
                right = middle
            else:
                return students[middle]
        return None
        
students = [Student(id) for id in range(0,100)]
print(linear_search(students, 5))
print(binary_search(students, 5))