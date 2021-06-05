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
    n, m, b = map(int, input().strip().split())
    arr = []
    for i in range(n):
        temp = list(map(int, input().strip().split()))
        arr.append(temp)
    
    pow_tow_n = 2**n
    n_binarr = []
    for i in range(1, pow_tow_n):
        temp = bin(i)[2:]
        l = len(temp)
        temp = "0"*(n - l) + temp
        n_binarr.append(temp)
    
    pow_tow_m = 2**m
    m_binarr = []
    for i in range(1, pow_tow_m):
        temp = bin(i)[2:]
        l = len(temp)
        temp = "0"*(m - l) + temp
        m_binarr.append(temp)
    
    res = 0
    
    for i in range(len(n_binarr)):
        for j in range(len(m_binarr)):
            temp = 0
            for k in range(len(n_binarr[i])):
                for l in range(len(m_binarr[j])):
                    if n_binarr[i][k] == "1" and m_binarr[j][l] == "1":
                        temp += arr[k][l]
            if temp == b:
                res += 1
                # print(n_binarr[i], m_binarr[j])
    print(res)
    return


t = 1
t = get_int()

for _ in range(t):
    solve()

# sub 1
