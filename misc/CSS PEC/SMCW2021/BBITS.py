"""

"""

import sys
from math import sqrt

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



def solve():
    n, k = get_ints()
    ones = bin(k)[2:].count("1")
    zero = bin(k)[2:].count("0")
    res = 2*ones + 3*zero
    res *= n-1
    res += 1
    p_int(res)
    return


t = 1
# t = get_int()

for _ in range(t):
    solve()
