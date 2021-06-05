
t = int(input())

for _ in range(t):
    strr, p = input().strip().split()
    k = len(strr)
    p = int(p)
    strr = strr[:p*2]
    strr1 = list(strr[:p])
    strr2 = list(strr[p:])
    l = len(strr1) + len(strr2)
    res = 0
    all = "qwertyuiopasdfghjklzxcvbnm"
    main_dick = {}
    for i in all:
        main_dick[i] = 0
    for i in strr1:
        main_dick[i] += 1
    for i in strr2:
        main_dick[i] -= 1

    for i in main_dick.values():
        res += abs(i)
    print(res//2 + (k-l))
