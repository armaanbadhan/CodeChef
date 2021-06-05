
n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

pref = [0]*(n+1)

for i in range(n):
    pref[i+1] = pref[i] + arr[i]

res = pref[k]

for i in range(n-k+1):
    res = max(res, pref[i + k] - pref[i])

print(res)
