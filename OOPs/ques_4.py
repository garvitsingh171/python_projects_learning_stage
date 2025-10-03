class Shape():
    def __init__(self, shape):
        self.shape = shape
    class Triangle():
        def __init__(self, side1, side2, side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        def perimeter(self):
            return self.side1 + self.side2 + self.side3
        def area(self):
            s = (self.side1 + self.side2 + self.side3)/2
            return (s(s-self.side1)(self.side2)(self.side3))**0.5
    class Cirlce():
        def __init__(self, radius):
            self.radius = radius
        def perimeter(self):
            return 2 * 3.14 * self.radius
        def area(self):
            return 3.14 * (self.radius ** 2)
    class Square():
        def __init__(self, side):
            self.side = side
        def perimeter(self):
            return 4 * self.side
        def area(self):
            return self.side ** 2
        