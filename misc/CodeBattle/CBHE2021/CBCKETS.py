
t = int(input())

for _ in range(t):
    n, q = map(int, input().strip().split())
    arr = [0]*n + [0]
    for i in range(q):
        l, r, x = map(int, input().strip().split())
        arr[l] += x
        arr[r+1] -= x
    for i in range(1, n):
        arr[i] += arr[i-1]
    even = 0
    print(arr)
    for i in range(n):
        if arr[i]&1 == 0:
            even += 1
    print(even, n - even)
    if even&1:
        print(1)
    else:
        print(2)
