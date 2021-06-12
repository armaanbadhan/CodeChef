
try:
    n = int(input())
    arr = list(map(int, input().strip().split()))

    base = arr[0]
    profit = 0

    for i in range(1, len(arr)):
        if arr[i] > base:
            profit += arr[i] - base
            base = arr[i]
        else:
            base = arr[i]

    print(profit)
except:
    pass
