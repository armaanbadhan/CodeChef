
t = int(input())

for _ in range(t):
    n = int(input())
    prev = -1
    vis = set()
    ok = True
    while prev != n:
        prev = n
        if prev in vis:
            ok = False
            print(0)
            break
        vis.add(prev)
        res = 0
        for i in str(n):
            res += int(i)**2
        n = res
    if ok:
        print(1 if n == 1 else 0)
