
M = 1e9 + 7

n = int(input())
arr = list(map(int, input().strip().split()))
q = int(input())
qarr = list(map(int, input().strip().split()))

res = sum(arr)

for i in range(q):
    res *= 2
    res %= M
    res = int(res)
    print(res)
