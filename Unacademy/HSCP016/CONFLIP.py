
t = int(input())

for _ in range(t):
    g = int(input())
    for i in range(g):
        i, n, q = map(int, input().strip().split())
        res = n//2
        if n&1:
            res += abs(q - i)
        print(res)
