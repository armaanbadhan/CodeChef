t = int(input())

for _ in range(t):
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    for i in range(n):
        str = input().strip()
        ans = 0
        for i in range(k):
            if str[i] == '1':
                ans += arr[i]
        print(ans)