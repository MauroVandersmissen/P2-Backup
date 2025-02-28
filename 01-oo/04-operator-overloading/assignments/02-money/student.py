class Money:
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self,amount):
        # if amount < 0:
        #     raise RuntimeError("Amount cannot be negative")
        self.__amount = amount

    @property
    def currency(self):
        return self.__currency
    
    @currency.setter
    def currency(self,currency):
        self.__currency = currency

    def __add__(self,other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount + other.amount,self.currency)
    
    def __sub__(self,other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies!")
        return Money(self.amount - other.amount,self.currency)
    
    def __mul__(self,amount):
        return Money(self.amount * amount,self.currency)
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
# print(Money(10,"EUR") + Money(20,"EUR"))
# print(Money(10,"EUR") + Money(20,"USD"))
# print(Money(30,"EUR") - Money(10,"EUR"))
# print(Money(30,"EUR") - Money(10,"USD"))
# print(Money(20,"EUR") * 5)
