n = int(input("Enter the length of your array: "))
arr = list(map(int, input("Enter your array: ").split()))
low, mid, high = 0, 0, n-1
while mid <= high:
    if arr[mid] == 1:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 2:
        mid += 1
    elif arr[mid] == 3:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1
    print(*arr)