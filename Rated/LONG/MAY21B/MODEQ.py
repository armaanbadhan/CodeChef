import math


def findFactors(num):
    res = []
    i = 1
    s = int(math.sqrt(num))
    if s*s == num:
        res.append(s)
    while i*i < num:
        if num%i == 0:
            res.append(i)
            if num%(num//i) == 0:
                res.append(num//i)
        i += 1
    return res


t = int(input())

for _ in range(t):
    n, m = map(int, input().strip().split())

    res = 0
    vis = set()
    div = findFactors(m)
    
    noLessThanN = 0
    for i in div:
        if i <= n:
            noLessThanN += 1
    
    for b in range(1, n+1):
        d = m - m%b
        if m%b == 0:
            if 0 not in vis:
                res += noLessThanN
            vis.add(0)
            continue

        i = 1
        while i*i < d and d not in vis:
            if d%i == 0:
                res += 1
                print(d, i)
            if d//i == i:
                res += 1
                print(d, i)
            i += 1
        vis.add(d)
    
    print(res)

# eh kya hai bc
