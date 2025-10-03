arr = list(map(int, input("Enter the arr: ").split()))

dict = {}

for num in arr:
    if num in dict : 
        dict[num] += 1
    else : 
        dict[num] = 1



print(dict)