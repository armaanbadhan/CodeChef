
a, b = map(int, input().strip().split())

lo = 1
hi = min(a, b)

res = lo

while lo <= hi:
    mid = (lo + hi)//2
    if mid <= a+b - 2*mid:
        lo = mid + 1
        res = mid
    else:
        hi = mid - 1

print(res)
