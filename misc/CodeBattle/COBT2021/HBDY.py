
sqsum = lambda x : (x*(x+1)*(2*x+1))//6

t = int(input())

for _ in range(t):
    x = int(input())
    lo, hi = 1, 1e6
    ans = 1
    while lo <= hi:
        mid = (lo+hi)//2
        if sqsum(mid) <= x:
            ans = mid
            lo = mid+1
        else:
            hi = mid-1
    print(ans)
