
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    myarr = []
    for i in range(n):
        myarr.append([arr[i], i])
    myarr.sort()
    print(myarr)
