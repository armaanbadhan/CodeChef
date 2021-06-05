
def solve():
    n = int(input())
    m = int(input())
    arr = [0]*(m+1)
    for i in range(n):
        l, r = map(int, input().strip().split())
        arr[l-1] += 1
        arr[r] += -1
    for i in range(1, m):
        arr[i] = arr[i] + arr[i-1]
    max_ = 1
    for i in arr:
        if i > max_:
            max_ = i
    print(max_)


t = int(input())

for _ in range(t):
    solve()

# o(m)
# in arr, we store when class starts and ends
# prefix sum gives number of classes at that time
# max is ans
# best
