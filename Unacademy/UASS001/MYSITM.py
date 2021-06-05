
t = int(input())

for _ in range(t):
    n, h, w = map(int, input().strip().split())
    a = max(h, w)
    b = min(h, w)
    lo, hi = 1, a*n
    while lo <= hi:
        mid = (lo+hi)//2
        if (mid//a) * (mid//b) >= n:
            hi = mid - 1
        else:
            lo = mid + 1
    print(lo)
