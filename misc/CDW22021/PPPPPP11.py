
n = int(input())

arr = []

for i in range(n):
    a, b = map(int, input().strip().split())
    arr.append((a, b))

arr.sort(key=lambda x: x[0])

i = 0

exit = arr[0][1]

res = 1

while i < len(arr):
    if arr[i][0] >= exit:
        res += 1
        exit = arr[i][1]
    i += 1

print(res)
