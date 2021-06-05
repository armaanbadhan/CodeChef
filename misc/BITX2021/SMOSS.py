
p, t, a, b, x, y = map(int, input().strip().split())
found = False
for i in range(t):
    for j in range(t):
        if (a - i*x) + (b - j*y) == p:
            found = True
            break
    if found:
        break

if found:
    print("YES")
else:
    print("NO")
