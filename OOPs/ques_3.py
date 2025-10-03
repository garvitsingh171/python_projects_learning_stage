class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Not Defined"
my_calc = Calculator(14, 7)
print(my_calc.add())
print(my_calc.sub())
print(my_calc.mul())
print(my_calc.div())