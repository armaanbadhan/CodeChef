
def area(a, b, x):
    return x*(a-x)*(b-x)

t = int(input())

for _ in range(t):
    a, b = map(int, input().strip().split()))
    lo, hi = 0, min(a, b)
    while lo <= hi:
        m1 = lo + (hi-lo)//3
        m2 = hi - (hi-lo)//3
        if area(a, b, m1) > area