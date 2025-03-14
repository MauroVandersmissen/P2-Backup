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
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    
    @property
    def card_suit(self):
        return self.__suit
    
    @card_suit.setter
    def card_suit(self,suit):
        self.__suit=suit

    def __repr__(self):
        return f"Card({self.value}, {self.suit})"


people=[
    Person(name='John', age=14),
    Person(name='Marc', age=17),
    Person(name='Sophie', age=15),
    Person(name='Chris', age=17),
    Person(name='Morgan', age=15),
]

cards=[
    Card(value=2, suit='hearts'),
    Card(value=5, suit='clubs'),
    Card(value=4, suit='hearts'),
    Card(value=10, suit='hearts'),
]

def count(collection, condition):
    count=0
    for element in collection:
        if condition(element):
            count+=1
    return count

def indices_of(xs,condition):
    indices=[]
    for index,string in enumerate(xs):
        if condition(string):
            indices.append(index)
    return indices

# def count_older_than(people,min_age):
#     count=0
#     if is_older(min_age):
#         count+=1
#     return count

# def is_older(min_age):
#     for person in people:
#         if person.age>min_age:
#             return True
#         else:
#             return False

# def count_older_than(people,min_age):
#     count=0
#     for person in people:
#         def is_older(person,min_age):
#             return person.age>min_age
#         if is_older(person,min_age):
#             count+=1
#     return count

def count_older_than(people,min_age):
    def is_older(person):
        return person.age>=min_age
    return count(people,is_older)

# def indices_of_cards_with_suit(cards,suit):
#     indices=[]
#     for i in range(len(cards)):
#         if cards[i].suit==suit:
#             indices.append(i)
#     return indices

# def indices_of_cards_with_suit(cards,suit):
#     indices=[]
#     for i in range(len(cards)):
#         def has_suit(cards):
#             return cards[i].suit==suit
#         if has_suit(cards):
#             indices.append(i)
#     return indices

# def indices_of_cards_with_suit(cards,suit):
#     indices=[]
#     for i in range(len(cards)):
#         def has_suit(cards):
#             return cards[i].suit==suit
#         if has_suit(cards):
#             indices.append(i)
#     return indices_of(cards,has_suit)

def indices_of_cards_with_suit(cards,suit):
    def has_suit(card):
        return card.suit==suit
    return indices_of(cards,has_suit)

# print(count_older_than(people,15))
# print(indices_of_cards_with_suit(cards,"hearts"))