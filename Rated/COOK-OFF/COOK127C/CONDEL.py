
t = int(input())

for _ in range(t):
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    res = 0
    cnt = 0
    for i in range(n):
        res += arr[i]*(cnt+1)
        cnt += 1
        if cnt == k:
            cnt = 0
    print(res)
