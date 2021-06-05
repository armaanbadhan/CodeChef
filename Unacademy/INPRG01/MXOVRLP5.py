
def bisect_left(a, x, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo


def insort_left(a, x, lo):
    hi = len(a)
    lo = bisect_left(a, x, lo, hi)
    a.insert(lo, x)


t = int(input())

for _ in range(t):
    n = int(input())
    m = int(input())
    entry, exit = [], []
    for i in range(n):
        l, r = map(int, input().strip().split())
        insort_left(entry, l, 0)
        insort_left(exit, r, 0)
    res = 0
    curr = 0
    i, j = 0, 0
    while i < n and j < n:
        if entry[i] <= exit[j]:
            curr += 1
            i += 1
        else:
            curr -= 1
            j += 1
        res = max(res, curr)
    print(res)

# using modules increases time? :thonk:
# using module gave 1.81s
# writing finctions gave 1.51s
# prefix sum best
