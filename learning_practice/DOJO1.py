a = int(input())
b = input().split()
c = int(input())
for index,num in enumerate(b):
    if int(num) == c:
        print(index,end=" ")