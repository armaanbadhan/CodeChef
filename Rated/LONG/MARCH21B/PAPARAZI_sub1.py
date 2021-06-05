
slope = lambda x1, y1, x2, y2 : (y2-y1)/(x2-x1)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    res = 1
    for i in range(n-1):
        temp_res = 1
        fori = slope(i, arr[i], i+1, arr[i+1])
        for j in range(i+2, n):
            x = slope(i, arr[i], j, arr[j])
            if x >= fori:
                fori = x
                temp_res = j-i
        res = max(temp_res, res)
    print(res)

# subtask 1 passed
# compared slopes for every pair
# ans is j-i, when slope = (arr[j]-arr[i])/(j-i) -> max
