
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [i+1 for i in range(n)]
    rev = arr[::-1]
    print(*arr)
    i = 0
    while True:
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
        print(*arr)
        i += 1
        if arr == rev:
            break
