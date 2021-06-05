
n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

found = False

for i in arr:
    if i == k:
        found = True
        break

if found:
    print(1)
else:
    print(-1)
