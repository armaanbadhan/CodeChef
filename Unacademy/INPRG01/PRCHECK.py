
def isprime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if not n&1:
        return False
    if not n%3:
        return False
    i = 5
    sq = int(n**(0.5))
    while i <= sq:
        if not n%i:
            return False
        i += 2
        if not n%i:
            return False
    return True

n = int(input())

if isprime(n):
    print(1)
else:
    print(0)
