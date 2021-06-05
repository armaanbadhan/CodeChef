
S = "abcdefghijklmnopqrstuvwxyz"

t = int(input())

for _ in range(t):
    n, k = map(int, input().strip().split())
    s = S[:n]
    for i in range(k):
        i %= len(s)
        print(s[i:] + s[:i])
