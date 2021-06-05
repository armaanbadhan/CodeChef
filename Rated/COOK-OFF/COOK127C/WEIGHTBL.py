
t = int(input())

for _ in range(t):
    w1, w2, x1, x2, m = map(int, input().strip().split())
    if w1 + m*x1 <= w2 <= w1 + m*x2:
        print(1)
    else:
        print(0)