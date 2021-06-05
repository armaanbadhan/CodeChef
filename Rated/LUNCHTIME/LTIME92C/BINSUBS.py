t = int(input())
while t:
    n = int(input().strip())
    ar = list(input().strip())
    zz, oo = ar.count("0"), 0
    ans=min(zz, ar.count("1"))
    for i in ar:
        if i == "0":
            zz -= 1
        else:
            oo += 1
        ans = min(ans, oo + zz)
    print(ans)
    t -= 1