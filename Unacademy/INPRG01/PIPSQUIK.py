
t = int(input())

for _ in range(t):
    n, h, y1, y2, l = map(int, input().strip().split())
    res = 0
    for i in range(n):
        ti, xi = map(int, input().strip().split())
        if l > 0:
            if ti == 1:
                if h - y1 > xi:
                    l -= 1
                    if l == 0:
                        res -= 1
            else:
                if y2 < xi:
                    l -= 1
                    if l == 0:
                        res -= 1
            res += 1
    print(res)
