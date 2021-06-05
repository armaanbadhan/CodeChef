
t = int(input())

for _ in range(t):
    n = int(input())
    mex = (n-1)//2
    for i in range(1, n + 1):
        q = abs(i - mex - 1)
        k = abs(q - mex)
        if q:
            print(" "*k + "*" + " "*(2*q - 1) + "*")
        else:
            print(" "*k + "*")
