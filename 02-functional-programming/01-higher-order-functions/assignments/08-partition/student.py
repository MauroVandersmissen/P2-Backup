def partition(lst,condition):
    lst1=[]
    lst2=[]
    for item in lst:
        if condition(item):
            lst1.append(item)
        else:
            lst2.append(item)
    return (lst1,lst2)

def is_child(person):
    return person.age<18

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return f"{self.name} ({self.age})"
    
def children_and_adults(people):
    return partition(people,is_child)

people = [
    Person("John", 14),
    Person("Marc", 17),
    Person("Sophie", 15),
    Person("Chris", 18),
    Person("Morgan", 20)
]

children, adults = children_and_adults(people)
print("Children:", children)
print("Adults:", adults)