
t = int(input())

for _ in range(t):
    n = int(input())
    m = int(input())
    arr = [0]*(m)
    for i in range(n):
        l, r = map(int, input().strip().split())
        for j in range(l-1, r):
            arr[j] += 1
    print(max(arr))

# Gave TLE O() too high
