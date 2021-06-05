
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().strip().split()]

    lmao = sum(arr)
    res = sum(arr)

    for i in range(n):
        for j in range(i, n):
            res = max(res, lmao - 2*sum(arr[i:j+1]))

    print(res)
