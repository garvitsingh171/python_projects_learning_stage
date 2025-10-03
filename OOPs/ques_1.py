class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2 * 3.14 * self.radius
    def area(self):
        return 3.14 * ((self.radius)**2)
r = 5
my_circle = Circle(r)
print(my_circle.circumference())
print(my_circle.area())