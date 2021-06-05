
t = int(input())

for it in range(t):
    n, m, q = map(int, input().strip().split())
    d = {}
    for i in range(n):
        mylist = list(map(int,input().split()))
        for j in range(m):
            x = mylist[j]
            if x not in d:
                d[x] = [i, j]
    for iq in range(q):
        x = int(input())
        print(*d[x])
