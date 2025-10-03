class Shape():
    def __init__(self, shape):
        self.shape = shape
class Triangle(Shape):
        def __init__(self, side1, side2, side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        def perimeter(self):
            return self.side1 + self.side2 + self.side3
        def area(self):
            s = self.perimeter()/2
            return (s*(s - self.side1)*(s - self.side2)*(s - self.side3))**0.5
class Cirlce(Shape):
        def __init__(self, radius):
            self.radius = radius
        def perimeter(self):
            return 2 * 3.14 * self.radius
        def area(self):
            return 3.14 * (self.radius ** 2)
class Square(Shape):
        def __init__(self, side):
            self.side = side
        def perimeter(self):
            return 4 * self.side
        def area(self):
            return self.side ** 2

t = Triangle(10, 12, 15)
c = Cirlce(16)
s = Square(18)

print(t.perimeter(), t.area())
print(c.perimeter(), c.area())
print(s.perimeter(), s.area())
        