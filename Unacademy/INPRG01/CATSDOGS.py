
t = int(input())

for _ in range(t):
    c, d, l = map(int, input().strip().split())
    if l%4:
        print("no")
    else:
        l //= 4   # now l in the number of animals
        # when no cat sitting on top -> on ground d+c(max) -> d(min)
        # when max cats sitting on dogs -> on ground d+c-2d -> c-d(min) -> c+d(max)
        # 2 cases when all cats can sit, and when they cant
        if 2*d >= c:
            if d <= l <= d+c:
                print("yes")
            else:
                print("no")
        else:
            if c-d <= l <= c+d:
                print("yes")
            else:
                print("no")
