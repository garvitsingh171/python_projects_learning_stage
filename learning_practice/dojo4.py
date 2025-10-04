arr = [1, 2, 4, 3]
n = len(arr)
for i in range(n - 1):  # outer loop
    swapped = False
    for j in range(n - i - 1):  # inner loop
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
            swapped = True
    if not swapped:
        break  # stop early if no swaps
print(arr)