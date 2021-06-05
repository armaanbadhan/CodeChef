
l, p = map(int, input().strip().split())

apple = True

lo, hi = 0, l**2

for i in range(l):
    mid = (lo+hi)//2
    if mid == p:
        break
    elif mid > p:
        hi = mid-1
        if apple:
            pass
        else:
            pass
    elif mid < p:
        lo = mid + 1
        if apple:
            pass
        else:
            pass

print("Apple" if apple else "Banana")
