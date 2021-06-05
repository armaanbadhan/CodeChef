
def isprime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n&1 == 0:
        return False
    if n%3 == 0:
        return False
    i = 5
    till = int(n*(0.5))+1
    while i<till:
        if n%i == 0:
            return False
        i += 2
        if n%i == 0:
            return False
        i += 4
    return True


n = int(input())
i = 2
cnt = 0
arr = []

while cnt != n:
    if isprime(i):
        arr.append(i)
        cnt += 1
    i += 1

print(*arr)
