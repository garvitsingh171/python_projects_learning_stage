class Person():
    def __init__(self, name, country, dateofbirth):
        self.name = name
        self.country = country
        self.dateofbirth = dateofbirth
    def age(self):
        return 2025 - self.dateofbirth
n = "Jatin Kumar"
c = "India"
dob = 2006
my_person = Person(n,c,dob)
print(my_person.age())