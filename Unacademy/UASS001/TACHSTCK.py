
n, d = map(int, input().strip().split())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

arr.sort()
res = 0

i = 0
while i< n-1:
    if arr[i+1] - arr[i] <= d:
        res += 1
        i += 1
    i += 1

print(res)
