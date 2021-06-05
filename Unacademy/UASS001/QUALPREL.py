from bisect import bisect_right

t = int(input())

for _ in range(t):
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    print(bisect_right(arr, arr[k]))
