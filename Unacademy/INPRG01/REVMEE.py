
n = int(input())
org = list(map(int, input().strip().split()))
arr = [0]*n

for i in range(n):
    arr[n-1-i] = org[i]

print(*arr)