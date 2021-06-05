
t = int(input())

for _ in range(t):
    n, x = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    maxx = len(set(arr))
    dup = n - maxx
    dup -= x
    if dup >= 0:
        print(maxx)
    else:
        print(maxx + dup)
