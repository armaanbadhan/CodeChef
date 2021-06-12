
t = int(input())

for _ in range(t):
    n = int(input())
    a = n//2
    b = n - a
    while a and b % a:
        a -= 1
        b += 1
    if a and b:
        print(a, b)
    else:
        print(-1)
    