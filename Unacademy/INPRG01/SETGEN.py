import sys

def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def p_str(x): sys.stdout.write(x+"\n")
def p_int(x): sys.stdout.write(str(x) + "\n")
def p_arr(arr): sys.stdout.write(" ".join(map(str, arr)) + "\n")


def binarr(n):
    res = []
    for i in range(2**n):
        temp_res = []
        while i:
            temp_res.append(i%2)
            i //= 2
        res.append(temp_res + [0]*(n-len(temp_res)))
    return res


def p_subarr(n):
    arr = [i+1 for i in range(n)]
    bin = binarr(n)
    for i in bin:
        temp = []
        for j in range(n):
            if i[j] == 1:
                temp.append(arr[j])
        p_arr(temp)


def solve():
    n = get_int()
    p_subarr(n)


t = get_int()

for _ in range(t):
    solve()
