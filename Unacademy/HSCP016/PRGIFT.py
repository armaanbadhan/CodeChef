
t = int(input())

for _ in range(t):
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    x = 0
    for i in arr:
        if i%2 == 0:
            x += 1
    if k == 0:
        if x == n:
            print("NO")
        else:
            print("YES")
    else:
        if x >= k:
            print("YES")
        else:
            print("NO")
