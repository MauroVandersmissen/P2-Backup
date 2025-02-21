from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    @property
    def length(self):
        return self.__length
    
    @property
    def width(self):
        return self.__width
    
    @property
    def area(self):
        return self.length*self.width
    
    @property
    def perimeter(self):
        return 2*(self.length+self.width)
    
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    @property
    def side(self):
        super().length

class Ellipse(Shape):
    def __init__(self,major_radius,minor_radius):
        self.__major_radius=major_radius
        self.__minor_radius=minor_radius

    @property
    def major_radius(self):
        return self.__major_radius
    
    @property
    def minor_radius(self):
        return self.__minor_radius
    
    @property
    def area(self):
        return pi*self.major_radius*self.minor_radius
    
    @property
    def perimeter(self):
        if self.major_radius==self.minor_radius:
            return 2*pi*self.major_radius
        else:
            raise NotImplementedError
    
class Circle(Ellipse):
    def __init__(self,radius):
        super().__init__(radius,radius)

    @property
    def radius(self):
        super().major_radius
    
# rectangle=Rectangle(2,3)
# print(rectangle.area)
# print(rectangle.perimeter)
# square=Square(2)
# print(square.area)
# print(square.perimeter)
# ellipse=Ellipse(2,3)
# print(ellipse.area)
# print(ellipse.perimeter)
# circle=Circle(2)
# print(circle.area)
# print(circle.perimeter)