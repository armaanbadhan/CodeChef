
def hhcf(x, y):
   while y:
       x, y = y, x % y
   return x

def llcm(x, y):
    return x*y//hhcf(x, y)


n = int(input())
arr = list(map(int, input().strip().split()))

arr_lcm = []

for i in range(n):
    for j in range(1+i, n):
        arr_lcm.append(llcm(arr[i], arr[j]))

res = arr_lcm[0]

for i in range(1, len(arr_lcm)):
    res = hhcf(res, arr_lcm[i])

print(res)
