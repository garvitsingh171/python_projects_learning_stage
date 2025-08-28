# This is a simple calculator program
num1 = eval(input("Enter first number: "))
opr = input("Enter operator (+, -, *, /): ")
num2 = eval(input("Enter second number: "))
if opr == "+":
    result = num1 + num2
elif opr == "-":
    result = num1 - num2
elif opr == "*":
    result = num1 * num2
elif opr == "/":
    result = num1 / num2
else:
    result = "Invalid operator"
print("Result:", result)