
n = int(input())
inp = list(map(int, input().strip().split()))

arr = []

for i in range(n):
    arr.append((inp[i], i+1))

arr.sort()

for i in range(n//2):
    print(arr[i][1], arr[n - i - 1][1])
