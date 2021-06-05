
t = int(input())

for _ in range(t):
    a, b, k = map(int, input().strip().split())
    if k&1:
        print((a-b)*(k//2) + a)
    else:
        print((a-b)*(k//2))
