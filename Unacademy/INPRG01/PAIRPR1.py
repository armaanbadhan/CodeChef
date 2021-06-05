
def isprime(n):
    if n < 2: return False
    if n < 4: return True
    if n%2 == 0: return False
    if n%3 == 0: return False
    i = 5
    sq = int(n**0.5)
    while i <= sq:
        if n%i == 0:
            return False
        i += 2
        if n%i == 0:
            return False
        i += 4
    return True

t = int(input())

for _ in range(t):
    n = int(input())
    found = False
    for i in range(1, n):
        if isprime(i) and isprime(n-i):
            print(i, n-i)
            found = True
            break
    if not found:
        print(-1, -1)
