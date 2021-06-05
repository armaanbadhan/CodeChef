import sys

def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def p_int(x): sys.stdout.write(str(x) + "\n")


def solve():
    n, m, K = get_ints()
    arr =  [[0 for ii in range(m+1)] for jj in range(n+1)]

    for i in range(n):
        temp = get_array()
        for j in range(m):
            arr[i+1][j+1] = temp[j]

    # prefix sum
    for i in range(n+1):
        for j in range(1, m+1):
            arr[i][j] += arr[i][j-1]

    # prefix sum
    for i in range(m+1):
        for j in range(1, n+1):
            arr[j][i] += arr[j-1][i]


    def good(i, j, k, K):
        k += 1
        cnt = k*k
        pref = arr[i+k][j+k] - arr[i][j+k] - arr[i+k][j] + arr[i][j]
        return pref/cnt >= K


    res = 0

    x = min(n, m)

    for i in range(x):
        pass

    for i in range(n):
        for j in range(m):
            x = min(n, m)
            temp = 0
            for k in range(x):
                if good(i, j, k, K):
                    temp = x - k
                    break
            res += temp

    p_int(res)


t = get_int()

for _ in range(t):
    solve()
