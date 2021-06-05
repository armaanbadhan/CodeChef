from math import sqrt

def isprime(x):
    if x < 2:
        return False
    if x < 4:
        return True
    if not x&1:
        return False
    if not x%3:
        return False
    i = 5
    s = sqrt(x)//1 + 1
    while i <= s:
        if not x%i:
            return False
        i += 2
        if not x%i:
            return False
        i += 4
    return True


def no_of_prime(n):
    ans = 0
    while n > 1:
        if isprime(n):
            ans += 1
        n -= 1
    return ans


t = int(input())
for _ in range(t):
    x, y = map(int, input().strip().split())
    if no_of_prime(x) <= y:
        print('Chef')
    else:
        print('Divyam')

# sub 2
# TLE for sub 3?
