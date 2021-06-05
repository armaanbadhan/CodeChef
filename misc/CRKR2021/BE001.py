from math import factorial

t = int(input())

for _ in range(t):
    n, x, y = map(int, input().strip().split())
    res1 = factorial(n)//(factorial(n-x) * factorial(x))
    res2 = factorial(n)//(factorial(n-y) * factorial(y))
    print(res1 * res2)