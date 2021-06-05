t = int(input())

for _ in range(t):
    d, c = map(int, input().strip().split())
    a = sum(list(map(int, input().strip().split())))
    b = sum(list(map(int, input().strip().split())))
    dd = 1
    if a >= 150 and b >= 150:
        dd = d*2
    elif a >= 150 or b >= 150:
        dd = d
    if dd > c:
        print('YES')
    else:
        print("NO")
