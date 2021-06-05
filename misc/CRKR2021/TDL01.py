
n, x = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

for i in range(1, n):
    arr[i] += arr[i-1]


if arr[]