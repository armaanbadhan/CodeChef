"""

"""

import sys

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
    n, w, r = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    if r >= w:
        print("YES")
        return
    vis = set()
    mex = 0
    for i in range(n):
        if arr[i] in vis:
            mex += arr[i]
            vis.remove(arr[i])
        else:
            vis.add(arr[i])
    if r + mex + mex >= w:
        print("YES")
        return
    print("NO")
    return


t = 1
t = get_int()

for _ in range(t):
    solve()
