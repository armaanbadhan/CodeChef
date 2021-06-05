# O(nm^3) solution for testing
# O(nm * nm * nm)
# nm -> 1 (use prefix sum)
# binary search as the 2-D array is sorted?

# import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

# t = int(input()) # ? where loop

def solve():
    n, m, K = map(int, input().strip().split())
    arr =  [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(n):
        temp = list(map(int, input().strip().split()))
        for j in range(m):
            arr[i+1][j+1] = temp[j]


    for i in range(n+1):
        for j in range(1, m+1):
            arr[i][j] += arr[i][j-1]


    for i in range(m+1):
        for j in range(1, n+1):
            arr[j][i] += arr[j-1][i]


    # for a in arr:
    #     print(*a)

    calc = lambda i, j, k, l : arr[k+1][l+1] - arr[i][l+1] - arr[k+1][j] + arr[i][j]
    # indexes of org arr

    def avg(i, j, k):
        num = k*k + 2*k + 1
        return calc(i, j, i+k, j+k)/num


    def check(i, j, k, K):
        # print(avg(i, j, k))
        return avg(i, j, k) >= K


    ########################
    ###### k-i == l-j ######
    ########################
    # we know i, j; choose k; get j

    # square matrices
    # average
    # sorted
    # binary search
    # prefix sum
    '''
    while True:
        t = K
        q, w = map(int, input().strip().split())
        e = int(input())
        r = e - q + w
        print(check(q, w, e, t))
    '''

    res = 0

    for i in range(n):
        for j in range(m):
            for k in range(0, min(n-i, m-j)):
                # print(i, j, k, K)
                if check(i, j, k, K):
                    res += 1

    print(res)

    # expecting TLE
    # use binary search maybe?
    # break when res == 1?


t = int(input())

for _ in range(t):
    solve()
