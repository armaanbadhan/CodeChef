
n, y, x = map(int, input().strip().split())

query = [0]*n
till = 1

for i in range(n):
    di = int(input())
    query[i] = di
    if di > till:
        till = di

arr = [1]
new = [1]

for i in range(till):
    temp = arr[-1] * x
    arr.append(temp + arr[-1])
    new.append(temp)
    l = len(arr)
    if l > y:
        arr[-1] -= new[l - y - 1]


for i in query:
    print(arr[i - 1])
