
t = int(input())

for _ in range(t):
    a, n = map(int, input().strip().split())
    a = a%10
    if a == 0:
        print(0)
    elif a == 1:
        print(1)
    elif a == 2:
        if n == 1:
            print(2)
        elif n == 2:
            print(4)
        else:
            print(6)
    elif a == 3:
        if n == 1:
            print(3)
        elif n == 2:
            print(9)
        else:
            print(1)
    elif a == 4:
        if n == 1:
            print(4)
        else:
            print(6)
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        if n == 1:
            print(7)
        elif n == 2:
            print(9)
        else:
            print(1)
    elif a == 8:
        if n == 1:
            print(8)
        elif n == 2:
            print(4)
        else:
            print(6)
    elif a == 9:
        if n == 1:
            print(9)
        else:
            print(1)
