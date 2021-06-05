cnt = int(input())
n = 2
c = 0
while c < cnt:
    s = (n**(1/2))//1
    i = 2
    p = True
    while i <= s:
        if n % i == 0:
            p = False
            break
        else:
            i += 1
    if p:
        c += 1
        print(n, end=' ')
    n += 1