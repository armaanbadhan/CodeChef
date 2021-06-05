
n = int(input())

for i in range(n):
    q = 2*i+1
    for j in range(q):
        print(q-abs(j-i), end=" ")
    print()