
S = "abcdefghijklmnopqrstuvwxyz"

ARR = []

for i in range(26):
    ARR.append(S[i:] + S[:i])


t = int(input())

for _ in range(t):
    n, m = map(int, input().strip().split())
    for i in range(n):
        for j in range(m):
            i %= 26
            j %= 26
            print(ARR[i][j], end=" ")
        print()
