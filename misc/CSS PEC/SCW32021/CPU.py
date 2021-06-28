
t = int(input())

for _ in range(t):
    n = int(input())
    MEX = 1000005
    vis = [0]*MEX
    for i in range(n):
        a, b = map(int, input().strip().split())
        vis[a] += 1
        vis[b] -= 1
    res = vis[0]
    for i in range(1, MEX):
        vis[i] += vis[i-1]
        res = max(vis[i], res)
    print(res)
