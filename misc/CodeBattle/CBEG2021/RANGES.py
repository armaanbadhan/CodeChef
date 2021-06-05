
t = int(input())

for _ in range(t):
    try:
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        mex = arr[k-1] - arr[0]
        ind = 0
        for i in range(1, n - k + 1):
            if arr[i + k - 1] - arr[i] > mex:
                mex = arr[i + k - 1] - arr[i]
                ind = i
        print(*arr[ind:ind+k])
    except:
        pass
