class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if num <= self.__num_arrows:
            self.__num_arrows -= num
        else:
            raise ValueError("Not enough arrows")


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        super().use_arrows(3)
        return f"{target} was shot by 3 crossbow bolts"
        # if isinstance(target, Human):
        #     return f"{target.get_name()} was shot by 3 crossbow bolts"
        # elif isinstance(target, str):
        #     return f"{target} was shot by 3 crossbow bolts"
        # else:
        #     raise ValueError("Target must be a Human object or a string")

# robin = Crossbowman("Robin", 10)
# john = Human("target")
# print(robin.triple_shot(john))