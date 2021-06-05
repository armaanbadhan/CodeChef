
t = int(input())

for _ in range(t):
    n, m, k = map(int, input().strip().split())
    res = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            res ^= (k+i+j)
    print(res)