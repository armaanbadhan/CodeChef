
n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

res = []

for i in range(n):
    res.append([a[i], b[i]])

res.sort()
res.sort(key=lambda x : x[1], reverse=True)

for i in res:
    print(*i, end=' ')
    