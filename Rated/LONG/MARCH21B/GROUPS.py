
t = int(input())

for _ in range(t):
    s = input().strip()
    res = 0
    group = False
    for i in s:
        if i == '1':
            if group == False:
                res += 1
            group = True
        if i == '0':
            group = False
    print(res)
