
n = int(input())
arr = list(map(int, input().strip().split()))
k = int(input())

res = []

x = n%k

for i in range(0, n-x, k):
    temp = arr[i:i+k]
    temp.reverse()
    res += temp

res += arr[n-x:]

print(*res)
