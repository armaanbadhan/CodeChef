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
    arr = get_array()
    start, end = 0, 0
    temp_s, temp_e = 0, 0
    money = 0
    for i in range(n):
        if money + arr[i] - arr[start] <= k: # ?
            money += arr[i]
            end = i
    return


t = 1
# t = get_int()

for _ in range(t):
    solve()
