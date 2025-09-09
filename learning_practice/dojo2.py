n = input()
m = int(input())
n = n.split('.')
n = n[1]
if len(n) >= m:
    print(n[m-1])
else:
    print('0')