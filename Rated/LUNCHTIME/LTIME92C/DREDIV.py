t = int(input())
for asdf in range(t):
    n, k = map(int, input().strip().split())
    ar = list(map(int, input().strip().split()))
    for j in range(n):
        for q in range(n):
            if ar[j]+ar[q] % k == 0:
                