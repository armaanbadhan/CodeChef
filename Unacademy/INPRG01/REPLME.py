
def fun(arr):
    if len(arr) == 1:
        return arr[0]
    a, b, *arr = sorted(arr)
    arr.append((3*a + 2*b)%100)
    return fun(arr)


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

print(fun(arr))
