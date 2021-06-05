from math import sqrt, ceil

n = int(input())

mysum = 1
sqr = sqrt(n)
if sqr*sqr == n:
    mysum += sqr//1

for i in range(2, ceil(sqr)):
    if n%i == 0:
        mysum += i + n//i

if mysum == n: print("YES")
else: print("NO")
