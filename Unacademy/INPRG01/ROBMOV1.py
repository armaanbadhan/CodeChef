
t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().strip().split())
    x = c - a
    y = d - b
    res = ""
    if x > 0:
        res += "E"*x
    else:
        res += "W"*-x
    if y > 0:
        res += "N"*y
    else:
        res += "S"*-y
    print(len(res))
    print(res)