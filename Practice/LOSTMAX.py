t = int(input())
while t:
    t -= 1
    l = list(map(int, input().strip().split(" ")))
    ln = len(l)
    for i in l:
        if i == ln-1:
            l.remove(i)
            break
    l = sorted(l)
    print(l[-1])
