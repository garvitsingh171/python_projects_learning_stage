x = 5
y = 0
try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print('division by zero')