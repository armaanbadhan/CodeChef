t = int(input())

for _ in range(t):
    m, h = map(int, input().strip().split())
    bmi = m/h
    bmi /= h
    if bmi <= 18:
        print(1)
    elif bmi <= 24:
        print(2)
    elif bmi <= 29:
        print(3)
    else:
        print(4)
