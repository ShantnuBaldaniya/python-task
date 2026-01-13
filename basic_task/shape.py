class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r
class Rectangle(Shape):
    def __init__(self, len, b):
        self.len = len
        self.b = b

    def area(self):
        return self.len * self.b

    def perimeter(self):
        return 2 * (self.len + self.b)
c = Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

r = Rectangle(4, 6)
print("R Area:", r.area())
print("R Perimeter:", r.perimeter())
