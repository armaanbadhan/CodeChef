
n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

res = 0

for i in range(n):
    res += a[i]*b[i]

b.sort(key=lambda x: abs(x), reverse=True)

if b[0] > 0:
    print(res + k*b[0])
else:
    print(res - k*b[0])
