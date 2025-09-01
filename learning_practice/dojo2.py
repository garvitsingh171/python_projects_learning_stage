no_oper = int(input())
oper = input().split()
x = 0
for operator in oper:
    if operator.lower() == '-x' or operator == 'x-':
        x = x - 1
    elif operator == '+x' or operator == 'x+':
        x = x + 1
print(x)