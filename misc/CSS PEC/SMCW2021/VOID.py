"""

"""

import sys
from math import ceil, sqrt

# constants
M = 1e9 + 7

# fast input
def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

# fast output
def p_str(x): sys.stdout.write(x+"\n")
def p_int(x): sys.stdout.write(str(x) + "\n")
def p_arr(arr): sys.stdout.write(" ".join(map(str, arr)) + "\n")


def number_of_squares(l, b) -> int:
    res = ceil(max(l, b) / min(l, b))
    return res


def solve():
    # for sub 1
    l, b, h = get_ints()
    k = get_int()
    res = ceil(h/k)
    sq = number_of_squares(l, b)
    res*= sq
    p_int(res)
    return


t = 1
# t = get_int()

for _ in range(t):
    solve()
