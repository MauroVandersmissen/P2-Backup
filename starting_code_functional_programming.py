students = [
    {"name": "Alice", "subject": "Mathematics", "score": 85},
    {"name": "Bob", "subject": "Computer Science", "score": 78},
    {"name": "Charlie", "subject": "Mathematics", "score": 92},
    {"name": "Diana", "subject": "Computer Science", "score": 79},
    {"name": "Eve", "subject": "Mathematics", "score": 76},
]

def collect_scores(students):
    scores=[]
    for student in students:
        scores.append(student["score"])
    return scores

def collect_scores2(students):
    return [student["score"] for student in students]

# print(collect_scores(students))
# print(collect_scores2(students))

def filter_high_scores(students):
    high_scores=[]
    for student in students:
        if student["score"]>=80:
            high_scores.append(student)
    return high_scores

def filter_high_scores2(students,filter_function):
    return [student for student in students if filter_function(student)]

# print(filter_high_scores(students))
# print(filter_high_scores2(students,lambda student:student["score"]>=80))
# sorted_scores=sorted(students,key=lambda student:student["score"],reverse=True)
# print(filter_high_scores2(sorted_scores,lambda student:student["subject"]=="Mathematics"))
math_students=filter_high_scores2(students,lambda student:student["subject"]=="Mathematics")
print(sorted(math_students,key=lambda student:student["score"],reverse=True))