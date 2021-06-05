t = int(input())

for _ in range(t):
    n, m = map(int, input().strip().split())
    ln, lm = [], []
    ans = 0
    for i in range(n):
        x, y = map(int, input().strip().split())
        ln.append([x, y])
    for i in range(m):
        x, y = map(int, input().strip().split())
        lm.append([x, y])
    '''for i in range(n):
        for j in range(m):
            temp = min(ln[i][1], lm[j][1]) - max(ln[i][0], lm[j][0])
            if temp > 0:
                ans += temp
    print(ans)'''
    ln.sort()
    lm.sort()
    print(ln)
    print(lm)
