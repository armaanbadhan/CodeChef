
n, v = input().strip().split()
n = int(n)
v = int(float(v)*100)
arr = list(map(float, input().strip().split()))
arr.reverse()
res = 0

for i in range(n):
    arr[i] = int(arr[i] * 100)

for i in arr:
    if v >= i:
        temp = int(v/i)
        v -= temp*i
        res += temp
    if v == 0:
        break

if v != 0:
    print(0)
else:
    print(res)
