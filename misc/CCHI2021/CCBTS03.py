
t = int(input())

for _ in range(t):
    n, k = map(int, input().strip().split())
    myarr = list(map(int, input().strip().split()))
    myarr.sort(reverse=True)
    diff = [0]
    for i in range(1, n):
        diff.append(myarr[i-1]-myarr[i])
    diff.sort()
    print(sum(diff[:k]))
