
n = int(input())

i = 0
res = []

while i<n:
    res.append(10*((i//2) + 1))
    i += 1
    if i == n:
        break
    i += 1
    res.append(i)

print(*res)
