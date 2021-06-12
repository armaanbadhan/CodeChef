from math import sqrt

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        a = n//2
        b = n - a
        if a == b:
            print(a, b)
        else:
            i = n//2
            try:
                while (n-i) % i:
                    i -= 2
                print(n//i, n - n//i)
            except:
                print(1, n-1)

# n -> even answer -> n/2 n/2
# n -> odd -> (worst canse a == 1) -> 1 odd, 1 even -> larger even, 
# -1 only if n == 1
