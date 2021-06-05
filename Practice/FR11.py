t = int(input())
for asdf in range(t):
    n = int(input())
    a = 0
    l = []
    ele = 1
    index = 0
    while True:
        l.append(ele)
        if index % 3 == 1:
            ele = int(ele*2.5)
        elif index % 3 == 2:
            ele *= 4
        else:
            ele *= 10
        index += 1
        if ele > n:
            break

    l = l[::-1]

    for e in l:
        if n >= e:
            temp = n//e
            a += temp
            n -= e * temp
    print(a)
