from math import comb

t = int(input())
for i in range(t):
    n = int(input())
    n -= 1
    j = pow(2, n)
    j %= 1000000007
    print(j)