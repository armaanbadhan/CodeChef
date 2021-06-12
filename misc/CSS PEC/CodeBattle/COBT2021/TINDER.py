
t = int(input())

for _ in range(t):
    n = int(input())
    people = input().strip()
    res = 0
    mcnt, fcnt = 0, 0
    for i in people:
        if i == 'M':
            mcnt += 1
        else:
            fcnt += 1
        if mcnt == fcnt:
            res += 1
    print(res)
