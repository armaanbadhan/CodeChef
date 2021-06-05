
try:
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().strip().split())
        if n&1:
            x = n//2
            y = 1
        else:
            x = n//2
            y = 0
        moves = x+y
        while moves%k and x > 0:
            x -= 1
            y += 2
            # print(x, y, 2*x + y)
            moves += 1
        print(x+y if x > 0 else -1)
except:
    pass