t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    x = arr[-1]*arr[-2] + arr[-1] - arr[-2]
    z = arr[0]*arr[1] + arr[1] - arr[0]
    print(max(x, z))