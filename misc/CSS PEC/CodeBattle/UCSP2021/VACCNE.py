
n, m = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))


def good(mid, m, a, b):
    a_max = max(a)
    b_max = max(b)
    if b_max!=0:
        c = a_max - (mid//b_max)
    else:
        c = 0
    return c < m


lo = 0
hi = 10**18

while lo <= hi:
    mid = (hi + lo)//2
    
    if good(mid, m, a, b):
        hi = mid-1
        ans = mid
    else:
        lo = mid+1

print(lo)
