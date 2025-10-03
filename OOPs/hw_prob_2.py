class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (3.14 * (self.radius ** 2) * self.height)
    
    def surface_area(self):
        return (2 * 3.14 * self.radius * self.height)

r = 20
h = 50

my_cylinder = Cylinder(r,h)
print(my_cylinder.volume())
print(my_cylinder.surface_area())