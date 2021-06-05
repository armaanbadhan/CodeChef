
t = int(input())

for _ in range(t):
    n = int(input())
    for row in range(n):
        q = abs(row - (n-1)//2)
        print(" "*q + "*"*abs(n-q*2))

