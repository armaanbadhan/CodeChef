
t = int(input())

for _ in range(t):
    n = int(input())
    sq = int(n**(0.5))
    res = []
    for i in range(sq, 0, -1):
        for j in range(sq, i-1, -1):
            if i*i + j*j == n:
                res.append([i, j])
            if len(res) == 2: break
        if len(res) == 2: break
    if len(res) >= 2:
        print(*res[0], *res[1])
    else:
        print(-1, -1, -1, -1)
