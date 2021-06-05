import numpy as np
# import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")


t = int(input())

# for sub 1 -> t = 1, n = 1, p = 0, straight line


for _ in range(t):
    n, p = map(int, input().strip().split())
    # n -> planets, p -> gravity till
    x = [0]
    y = [0]
    for i in range(n):
        xi, yi = map(int, input().strip().split())
        x.append(xi)
        y.append(yi)
    if len(x) != len(set(x)):
        print("No")
        continue
    coeffs = np.polyfit(x=x, y=y, deg=n)
    # print(coeffs)
    res = []
    degSet = False
    deg = len(coeffs) - 1
    for i in coeffs:
        temp = round(i, 1)
        if temp == -0.0:
            temp = 0.0
        if temp != 0.0:
            degSet = True
        if degSet:
            res.append(temp)
        else:
            deg -= 1
    # print(np.poly1d(coeffs))
    print("Yes")
    print("Yes")
    print(*res)
    print(deg if deg > 0 else 0)
