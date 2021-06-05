
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    min_till_i = arr[0]
    res = min_till_i
    for i in range(1, n):
        if arr[i] < min_till_i:
            min_till_i = arr[i]
        res += min_till_i
    print(res)

# ez