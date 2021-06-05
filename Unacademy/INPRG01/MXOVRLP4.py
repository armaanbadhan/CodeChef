
t = int(input())

for _ in range(t):
    n = int(input())
    m = int(input())
    entry, exit = [], []
    for i in range(n):
        l, r = map(int, input().strip().split())
        entry.append(l)
        exit.append(r)
    entry.sort()
    exit.sort()
    res = 0
    curr = 0
    i, j = 0, 0
    while i < n and j < n:
        if entry[i] <= exit[j]:
            curr += 1
            i += 1
        else:
            curr -= 1
            j += 1
        res = max(res, curr)
    print(res)

# O(n logn)
# ~counting inversions
