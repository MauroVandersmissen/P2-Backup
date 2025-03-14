class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age=age
    
    # def __lt__(self,other):
    #     return self.age<other.age
    
    def __repr__(self):
        return f'{self.name} ({self.age})'
    
people=[
    Person(name='John', age=14),
    Person(name='Marc', age=17),
    Person(name='Sophie', age=15),
    Person(name='Chris', age=17),
    Person(name='Morgan', age=15),
    Person(name='John', age=8)
]
    
def sort_by_age(people):
    return sorted(people,key=lambda person:person.age)

def sort_by_decreasing_age(people):
    return sorted(people,key=lambda person:person.age,reverse=True)

def sort_by_name(people):
    return sorted(people,key=lambda person:person.name)

def sort_by_name_then_age(people):
    return sorted(people,key=lambda person:(person.name,person.age))

def sort_by_name_then_decreasing_age(people):
    return sorted(people,key=lambda person:(person.name,-person.age))

print(sort_by_age(people))
print(sort_by_decreasing_age(people))
print(sort_by_name(people))
print(sort_by_name_then_age(people))
print(sort_by_name_then_decreasing_age(people))