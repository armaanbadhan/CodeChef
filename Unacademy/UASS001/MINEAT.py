import sys

def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def p_str(x): sys.stdout.write(x+"\n")
def p_int(x): sys.stdout.write(str(x) + "\n")
def p_arr(arr): sys.stdout.write(" ".join(map(str, arr)) + "\n")


def good(arr, k, h, n):
    res = n
    for i in arr:
        res += i//k
        if i%k == 0:
            res -= 1
    return h >= res


def solve():
    n, h = get_ints()
    arr = get_array()
    lo, hi = 1, sum(arr)
    while lo <= hi:
        mid = (lo+hi)//2
        if good(arr, mid, h, n):
            hi = mid - 1
        else:
            lo = mid + 1
    p_int(lo)


t = get_int()

for _ in range(t):
    solve()
