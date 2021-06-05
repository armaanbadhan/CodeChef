import sys

def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def p_str(x): sys.stdout.write(x+"\n")
def p_int(x): sys.stdout.write(str(x) + "\n")
def p_arr(arr): sys.stdout.write(" ".join(map(str, arr)) + "\n")


def solve():
    n, k = get_ints()
    arr = get_array()
    arr.sort()
    res = arr[k-1] - arr[0]
    for i in range(n-k+1):
        res = min(res, arr[i+k-1] - arr[i])
    p_int(res)


t = get_int()

for _ in range(t):
    solve()
