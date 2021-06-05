import sys

def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def p_str(x): sys.stdout.write(x+"\n")
def p_int(x): sys.stdout.write(str(x) + "\n")
def p_arr(arr): sys.stdout.write(" ".join(map(str, arr)) + "\n")


def p_subarr(n):
    subsets = [[]]
    for i in range(n):
        for ii in range(0, 2**i):
            subsets.append(subsets[ii]+[i+1])
    for i in subsets:
        p_arr(i)


def solve():
    n = get_int()
    p_subarr(n)


t = get_int()

for _ in range(t):
    solve()
