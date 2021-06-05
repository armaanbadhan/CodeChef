
n = input().strip()

l = len(n)
res = True

for i in range(l//2):
    if n[i] != n[l-1-i]:
        res = False
        break

if res:
    print("YES")
else:
    print("NO")
