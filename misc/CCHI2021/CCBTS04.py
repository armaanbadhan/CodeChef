
t = int(input())

for _ in range(t):
    n = int(input())
    height = list(map(int, input().strip().split()))
    iq = list(map(int, input().strip().split()))
    ans = 1
    max_h, min_i = height[0], iq[0]
    for i in range(1, n):
        if max_h < height[i] and min_i > iq[i]:
            ans += 1
            max_h = height[i]
            min_i = iq[i]
    print(ans)
