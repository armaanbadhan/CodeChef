from decimal import *
# import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")


def solve():
    n = int(input())
    d = int(input())
    getcontext().prec = 510
    res = Decimal(Decimal(n)).sqrt()
    res = str(res)
    if "." in res:
        res = res.split(".")
        print(res[0], end=".")
        print(res[1][:d])
    else:
        print(res, end=".")
        print("0"*d)


t = int(input())

for _ in range(t):
    solve()
