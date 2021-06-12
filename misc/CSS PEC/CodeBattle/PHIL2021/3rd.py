
n = int(input())
arr = list(map(int, input().strip().split()))

arr.sort()

res = 0

for i in range(1, n):
    res += arr[i] - arr[0]

print(res)
