t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    vals=[]
    for i in range(n):
        vals.append((-a[i],i))
    vals.sort()
    ans = [0]*n
    c = 1
    for i in vals:
        ans[i[1]]=c
        c += 1
    print(*ans)
