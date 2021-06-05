from math import ceil, floor

t = int(input())

for _ in range(t):
    r, n, t = map(int, input().strip().split())
    t -= 1
    inp = list(map(int, input().strip().split()))
    arr = []
    for i in inp:
        arr.append(ceil(i/2))
        arr.append(floor(i/2))
    print(arr)
    print(sum(arr[:t]))
    print("YES" if sum(arr[:t]) > r else "NO")
    