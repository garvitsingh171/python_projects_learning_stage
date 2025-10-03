arr = list(map(int, input("Enter the arr: ").split()))
cand = None
count = 0
for num in arr:
    if count == 0:
        cand = num
        count += 1
    elif num == cand:
        count += 1
    else:
        count -= 1
no = 0
for num in arr:
    if num == cand:
        no += 1
if (len(arr) // 2) < no:
    print(cand)
else:
    print(-1)