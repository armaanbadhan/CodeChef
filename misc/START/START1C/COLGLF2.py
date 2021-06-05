t = int(input())

for _ in range(t):
    s = int(input())
    intro = list(map(int, input().strip().split()))
    ans = 0
    for i in range(s):
        arr = list(map(int, input().strip().split()))
        ans += sum(arr[1:])
        ans -= (arr[0]-1)*intro[i]
    print(ans)