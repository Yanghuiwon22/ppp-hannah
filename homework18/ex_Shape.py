import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return (self.w + self.h)*2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        total = self.a+self.b+self.c
        return math.sqrt(total*(total-self.a)*(total-self.b)*(total-self.c))

    def perimeter(self):
        return a+b+c



class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r * 2 * math.pi

    def perimeter(self):
        return math.pi * self.r * self.r

class HexagonRegualr(Shape):
    def __init__(self, l):
        self.l = l

    def area(self):
        return (0.5*self.l*(self.l/2)*math.sqrt(3))*6

    def perimeter(self):
        return self.l*6

def main():
    shapes = [
        Rectangle(5, 2),
        Rectangle(8, 5),
    ]
    for shape in shapes:
        print(f"넓이는 : {shape.area()}")
        print(f"둘레는 : {shape.perimeter()}")


if __name__=="__main__":
    main()