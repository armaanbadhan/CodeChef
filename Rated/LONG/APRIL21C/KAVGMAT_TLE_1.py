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
        # print(pref)
        return pref/cnt >= K


    res = 0
    x = min(n, m)

    for k in range(x):
        i = n-1-k
        j = 0
        while (i >= 0) and (j < m-k):
            temp = 0
            if good(i, j, k, K):
                temp = m - j - k
                i -= 1
            else:
                j += 1
            res += temp
            # print(temp, res, i, j, k)
    p_int(res)


t = get_int()

for _ in range(t):
    solve()
