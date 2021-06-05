t = int(input())
k = int(input())
ar = list(map(int, input().strip().split(' ')))
ar = sorted(ar)
ans = 0

for j in range(k):
    if ar[j] < 0:
        ar[j] *= -1

for i in range(t):
    if ar[i] > 0:
        ans += ar[i]

print(ans)