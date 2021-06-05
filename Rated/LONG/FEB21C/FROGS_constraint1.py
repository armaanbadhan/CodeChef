for _ in range(int(input())):
    n = int(input())
    w1, w2 = map(int, input().strip().split())
    l1, l2 = map(int, input().strip().split())
    ans = 0
    if w1 < w2:
        print(0)
    else:
        if l1 == 1:
            print(2)
        else:
            print(1)
# for n == 2
