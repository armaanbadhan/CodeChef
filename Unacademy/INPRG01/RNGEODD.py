
l, r = map(int, input().strip().split())

if not l&1:
    l += 1

res = []

while l <= r:
    res.append(l)
    l += 2

print(*res)