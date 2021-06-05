from math import sqrt
t = int(input())

e, s = "Elevator", "Stairs"
rt2 = sqrt(2)

for _ in range(t):
    n, v1, v2 = map(int, input().strip().split())
    if rt2*v1 > v2:
        print(s)
    else:
        print(e)
