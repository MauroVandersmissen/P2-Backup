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

def group_by_age(people):
    grouped={}
    for person in people:
        age=person.age
        if age in grouped:
            grouped[age].append(person)
        else:
            grouped[age]=[person]
    return grouped
                

def group_by_suit(cards):
    grouped={}
    for card in cards:
        suit=card.suit
        if suit in grouped:
            grouped[suit].append(card)
        else:
            grouped[suit]=[card]
    return grouped


def group_by(xs,key_function):
    grouped={}
    for item in xs:
        key=key_function(item)
        if key in grouped:
            grouped[key].append(item)   
        else:
            grouped[key]=[item]
    return grouped

def get_person_age(person):
    return person.age

def get_card_suit(card):
    return card.suit

# print(group_by_age(people))
# print(group_by_suit(cards))
print(group_by(people,get_person_age))
print(group_by(cards,get_card_suit))