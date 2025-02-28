class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def can_be_sold_to(self, customer):
        return True
    
class AgeRestrictedItem(Item):
    def __init__(self, name, price, min_age=18):
        super().__init__(name, price)
        self.min_age = min_age

    def can_be_sold_to(self, customer):
        return customer.age >= self.min_age
    
class CountryRestrictedItem(Item):
    def __init__(self, name, price, country="Arstotzka"):
        super().__init__(name, price)
        self.country = country

    def can_be_sold_to(self, customer):
        return customer.country != self.country

class Customer:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


class ShoppingList:
    def __init__(self, owner):
        self.__owner = owner
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def add(self, item):
        if not item.can_be_sold_to(self.owner):
            raise ValueError()
        self.__items.append(item)