
arr = list(map(int, input().strip().split()))

arr.reverse()

max = arr[0]

for i in range(len(arr)):
    if arr[i] <= max:
        arr[i] = max
    else:
        max = arr[i]

arr.reverse()

indexlist = []
idx = 0

for i in range(1, len(arr)):
    if arr[i-1] != arr[i]:
        indexlist.append(idx)
    idx += 1

indexlist.append(len(arr)-1)


print(*arr)
print(*[i for i in range(len(arr))])
print(indexlist)
