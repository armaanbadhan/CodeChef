from bisect import bisect_left

i = 1

arr = []

while i*i <= 1000000000:
    arr.append(i*i)
    i += 1

t = int(input())

for _ in range(t):
    n = int(input())
    i = bisect_left(arr, n+1)
    print(*arr[:i])
